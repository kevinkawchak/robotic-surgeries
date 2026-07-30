"""Figure 24. Everything recorded about you, where it goes, and who can read it.

Type
    Diagrams (Python)-type, data pipeline with an access-control overlay.

Paper section
    Section 9, Your Visits, Your Data, Your Robot Instructions.

Patient concern answered
    ChatGPT concern 10 (privacy, recording, and secondary data use) and concern
    16 (post-trial burdens); Gemini family 4. Consent forms describe data
    handling in a paragraph that lists categories and omits the pipeline. The
    question a participant actually asks is narrower and harder: who, by name or
    by role, can open the file that contains the video of my operation.

Why this diagram type
    A pipeline is a directed sequence of stages with a store at each stage and a
    principal attached to each store. mingrammer/diagrams renders exactly that,
    and its cluster idiom lets the access boundary be drawn as a region rather
    than asserted as a label.

TikZ rendering notes for full-patient
    Draw with the dg* vocabulary of patientstyle.sty.
    Four left-to-right stages as dgcluster containers at x centres -6.6, -1.4,
    3.8, 9.4, plus one dgcluster2 access-control container spanning the full
    width at y -7.8.
    Every node is a \\dgnode call; tile pitch 2.4 cm horizontal, 2.2 cm
    vertical, so at least 13 mm of clear space separates tile edges.
    Pictograms: \\glyphsignal for capture, \\glyphdoc for the case report form,
    \\glyphlock for the hash chain, \\glyphdb for each store, \\glyphuser for
    each principal, \\glyphshield for de-identification, \\glyphchart for the
    analysis outputs.
    A principal that can read a store is joined to it by a solid dgedgeb line;
    a principal that cannot is joined by nothing at all. Absence of an edge is
    the access statement, and the figure says so in a foot note.
    Retention periods are set in \\tiny\\sffamily\\itshape beneath each store
    tile's label, on a third line, so they never require a leader.
    Cross-stage edges are straight; the two feedback edges from the access
    container use to[out=90,in=-90,looseness=0.8].
"""

from __future__ import annotations

PROTO_BLUE = "#00417A"
PROTO_GRAY = "#6C757D"
PROTO_WHITE = "#FFFFFF"
PROTO_BLACK = "#000000"
PA_BLUE_1 = "#3C7DB2"
PA_BLUE_2 = "#DCE8F1"
PA_GRAY_L = "#E9ECEF"
PA_GRAY_M = "#CED4DA"
PA_GRAY_D = "#9AA1A8"

GRAPH_ATTR = {
    "fontname": "Helvetica",
    "fontsize": "12",
    "bgcolor": PROTO_WHITE,
    "pad": "0.45",
    "nodesep": "0.85",
    "ranksep": "1.2",
}

NODE_ATTR = {"fontname": "Helvetica", "fontsize": "10", "fontcolor": "#111111"}
EDGE_ATTR = {"fontname": "Helvetica", "fontsize": "9", "color": PROTO_GRAY}

# Retention is stated per store, in days, because "retained as required" is not
# an answer to the question the participant asked.
RETENTION_DAYS = {
    "raw_telemetry": 3650,
    "operative_video": 3650,
    "case_report_form": 5475,
    "hash_chain": 5475,
    "identified_store": 5475,
    "deidentified_store": 3650,
    "analysis_outputs": 5475,
}

# Who can read what. A role absent from a list cannot read that store, and the
# figure draws no edge for it. This dictionary is the figure's access statement.
READ_ACCESS = {
    "raw_telemetry": ("site PI", "sponsor-investigator", "you, on request"),
    "operative_video": ("operating surgeon", "site PI", "you, on request"),
    "case_report_form": ("site PI", "CRO monitor", "you, on request"),
    "hash_chain": ("sponsor-investigator", "FDA on inspection", "you, on request"),
    "identified_store": ("site PI", "you, on request"),
    "deidentified_store": ("sponsor-investigator", "DSMB", "statistician"),
    "analysis_outputs": ("everyone above", "and the public, at publication"),
}


def build() -> None:
    """Render the figure. No-op when mingrammer/diagrams is not installed."""
    try:
        from diagrams import Cluster, Diagram, Edge
        from diagrams.generic.storage import Storage
        from diagrams.programming.flowchart import (
            Action,
            Document,
            InputOutput,
            PredefinedProcess,
        )
    except ImportError:
        return

    with Diagram(
        "Figure 24. Your data, stage by stage, with the read list on every store",
        filename="fig_24_data_pipeline",
        show=False,
        direction="LR",
        outformat="svg",
        graph_attr=GRAPH_ATTR,
        node_attr=NODE_ATTR,
        edge_attr=EDGE_ATTR,
    ):
        with Cluster("1. Capture, in the room", graph_attr={"bgcolor": PA_BLUE_2}):
            telemetry = InputOutput(
                "Arm motion, tip force,\nvessel proximity\n640 channels"
            )
            video = InputOutput("Operative video\nand endoscope feed")
            clinical = InputOutput("Vitals, labs, CA 19-9,\ndrain output")

        with Cluster("2. Write once, edit never", graph_attr={"bgcolor": PA_GRAY_L}):
            chain = PredefinedProcess(
                f"Hash chain\n21 CFR part 11\n{RETENTION_DAYS['hash_chain'] // 365} year retention"
            )
            crf = Document(
                f"Case report form\n{RETENTION_DAYS['case_report_form'] // 365} year retention"
            )
            telemetry >> Edge(color=PROTO_GRAY) >> chain
            video >> Edge(color=PROTO_GRAY) >> chain
            clinical >> Edge(color=PROTO_GRAY) >> crf
            crf >> Edge(color=PROTO_GRAY) >> chain

        with Cluster("3. Two stores, one boundary", graph_attr={"bgcolor": PA_GRAY_L}):
            identified = Storage(
                f"Identified store\nname, MRN, images\n{RETENTION_DAYS['identified_store'] // 365} years"
            )
            deident = Action("De-identification\nHIPAA safe harbour")
            deidentified = Storage(
                f"De-identified store\n{RETENTION_DAYS['deidentified_store'] // 365} years"
            )
            chain >> Edge(color=PROTO_GRAY) >> identified
            identified >> Edge(color=PROTO_BLUE, label="one way") >> deident
            deident >> Edge(color=PROTO_BLUE) >> deidentified

        with Cluster("4. What leaves", graph_attr={"bgcolor": PA_GRAY_M}):
            analysis = Storage("Analysis outputs\ntables and figures")
            regulatory = Document("Regulatory reports\nFDA, IRB, DSMB")
            publication = Document("Publication\nno identifiers")
            yours = Document("Your own copy\non request, any time")
            deidentified >> Edge(color=PROTO_GRAY) >> analysis
            analysis >> Edge(color=PROTO_GRAY) >> regulatory
            analysis >> Edge(color=PROTO_GRAY) >> publication
            identified >> Edge(color=PROTO_BLUE, label="always available") >> yours

        with Cluster("Who may read each store", graph_attr={"bgcolor": PA_GRAY_L}):
            you = Document("You\nevery store above")
            site_pi = Document("Site PI\nidentified and de-identified")
            sponsor = Document("Sponsor-Investigator\nde-identified plus the chain")
            dsmb = Document("DSMB\nde-identified only")
            fda = Document("FDA on inspection\nchain and CRF")
            you >> Edge(color=PROTO_BLUE, style="dashed") >> identified
            site_pi >> Edge(color=PROTO_GRAY, style="dashed") >> identified
            sponsor >> Edge(color=PROTO_GRAY, style="dashed") >> deidentified
            dsmb >> Edge(color=PROTO_GRAY, style="dashed") >> deidentified
            fda >> Edge(color=PROTO_GRAY, style="dashed") >> chain

        # Two things that are NOT in this pipeline, drawn as an explicit absence.
        (
            deidentified
            >> Edge(
                color=PROTO_BLACK,
                style="dashed",
                label="no commercial model training without separate consent",
            )
            >> publication
        )


if __name__ == "__main__":
    build()
