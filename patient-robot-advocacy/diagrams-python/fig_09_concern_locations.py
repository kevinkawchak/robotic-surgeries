"""Figure 9. Where each documented concern physically lives in the trial system.

Type
    Diagrams (Python)-type, clustered node map.

Paper section
    Section 3, The Documented Patient Concerns.

Patient concern answered
    All twenty-one, by giving each one a physical address. A concern that has no
    address is unanswerable; a concern that resolves to a named cabinet, a named
    console, or a named cable can be inspected. Gemini families 2, 3, and 4 and
    ChatGPT concerns 1, 10, 11, and 13 are the ones that only become tractable
    once the reader knows which box they are about.

Why this diagram type
    mingrammer/diagrams is the only permitted type whose whole idiom is physical
    deployment: clusters are rooms and racks, nodes are machines, edges are
    cables. A flowchart can say "the model is on premises"; only an
    infrastructure diagram can show that the box it runs in has no edge leaving
    the building.

TikZ rendering notes for full-patient
    Draw with the dg* vocabulary of patientstyle.sty.
    Four dgcluster containers: operating_room at x centre -5.4, on_prem at
    x centre 1.8, governance at x centre 8.6, outside_world at x centre 8.6
    lower. Cluster inner sep 7pt so no tile touches a border.
    Each node is a \\dgnode call: a 9 mm rounded tile carrying a vector
    pictogram, with a \\tiny\\sffamily label set beneath it via the automatically
    defined <name>l node. Tile pitch 2.4 cm horizontally and 2.2 cm vertically,
    which leaves at least 13 mm of clear space between tile edges and 6 mm
    between a label and the tile beneath it.
    Concern badges are 4.6 mm pagraym discs with a \\tiny numeral, anchored
    north east on their tile with a 1 mm outset, so a badge never overlaps a
    label.
    The single cut edge between on_prem and outside_world is drawn as a
    dgedged dashed line terminated by a 3 mm protoblack cross glyph, labelled
    "no route exists during a procedure".
    Cross-cluster edges use to[out=0,in=180,looseness=0.85]; edges inside a
    cluster are straight.
"""

from __future__ import annotations

PROTO_BLUE = "#00417A"
PROTO_GRAY = "#6C757D"
PROTO_WHITE = "#FFFFFF"
PA_BLUE_1 = "#3C7DB2"
PA_BLUE_2 = "#DCE8F1"
PA_GRAY_L = "#E9ECEF"
PA_GRAY_M = "#CED4DA"
PA_GRAY_D = "#9AA1A8"

GRAPH_ATTR = {
    "fontname": "Helvetica",
    "fontsize": "12",
    "bgcolor": PROTO_WHITE,
    "pad": "0.4",
    "nodesep": "0.9",
    "ranksep": "1.1",
    "splines": "ortho",
}

NODE_ATTR = {
    "fontname": "Helvetica",
    "fontsize": "10",
    "fontcolor": "#111111",
}

EDGE_ATTR = {
    "fontname": "Helvetica",
    "fontsize": "9",
    "color": PROTO_GRAY,
}

# Concern number -> the physical component that answers it. The badge on each
# tile in the rendered figure carries these numerals, so a reader can move from
# Figure 5 (the concern list) to a specific box without an intermediate lookup.
CONCERN_ADDRESS = {
    1: "console",  # who is actually driving
    2: "console",  # can the surgeon stop it, and how fast
    3: "console",  # will the surgeon defer to the model
    6: "arms",  # malfunction or unintended motion
    7: "vision",  # misreading tissue or a margin
    8: "gate",  # injury to a major vessel
    9: "arms",  # instrument failure mid-procedure
    10: "console",  # conversion to open surgery
    15: "recorder",  # who sees the recording
    16: "vault",  # will my data train other systems
    17: "boundary",  # could the system be attacked
    19: "registry",  # can the software change after I consent
    20: "audit",  # who is accountable if I am harmed
}


def build() -> None:
    """Render the figure. No-op when mingrammer/diagrams is not installed."""
    try:
        from diagrams import Cluster, Diagram, Edge
        from diagrams.generic.compute import Rack
        from diagrams.generic.device import Tablet
        from diagrams.generic.network import Firewall, Switch
        from diagrams.generic.storage import Storage
        from diagrams.programming.flowchart import Decision, Document, InputOutput
    except ImportError:
        return

    with Diagram(
        "Figure 9. Where each documented concern physically lives",
        filename="fig_09_concern_locations",
        show=False,
        direction="LR",
        outformat="svg",
        graph_attr=GRAPH_ATTR,
        node_attr=NODE_ATTR,
        edge_attr=EDGE_ATTR,
    ):
        with Cluster(
            "Operating room, sterile field", graph_attr={"bgcolor": PA_BLUE_2}
        ):
            arms = Rack("Eight robotic arms\nforce-capped\n[6, 9]")
            vision = InputOutput("Vision and sensor stack\n640 channels, 10 kHz\n[7]")
            console = Tablet("Surgeon console\nsole approval authority\n[1, 2, 3, 10]")
            recorder = Document("Procedure recorder\nvideo, motion, force\n[15]")
            console >> Edge(color=PROTO_BLUE, label="approved motion only") >> arms
            vision >> Edge(color=PROTO_GRAY, label="field state") >> console
            arms >> Edge(color=PROTO_GRAY) >> recorder

        with Cluster(
            "On-premises cabinet, same building", graph_attr={"bgcolor": PA_GRAY_L}
        ):
            model = Rack("On-premises LLM\nadvisory, no actuator path")
            gate = Decision("Deterministic safety gate\nforce and no-fly test\n[8]")
            registry = Storage("Version registry\nfrozen at your consent\n[19]")
            audit = Storage("Hash-chained audit trail\n21 CFR part 11\n[20]")
            vault = Storage("Data vault\nretention and use policy\n[16]")
            model >> Edge(color=PROTO_GRAY, style="dashed") >> gate
            gate >> Edge(color=PROTO_BLUE, label="passed plans only") >> console
            registry >> Edge(color=PROTO_GRAY) >> model
            recorder >> Edge(color=PROTO_GRAY) >> vault
            gate >> Edge(color=PROTO_GRAY) >> audit

        with Cluster(
            "Governance, off the critical path", graph_attr={"bgcolor": PA_GRAY_L}
        ):
            dsmb = Document("DSMB\ncohort-boundary review")
            irb = Document("IRB\ncomplaint route open to you")
            sponsor = Document("Sponsor-Investigator\nnamed accountable party")
            audit >> Edge(color=PROTO_GRAY, style="dashed") >> dsmb
            audit >> Edge(color=PROTO_GRAY, style="dashed") >> sponsor
            vault >> Edge(color=PROTO_GRAY, style="dashed") >> irb

        with Cluster(
            "Everything outside the building", graph_attr={"bgcolor": PA_GRAY_M}
        ):
            boundary = Firewall(
                "Network boundary\nclosed for the whole procedure\n[17]"
            )
            external = Switch("Hospital network,\ncloud, vendor support")
            (
                boundary
                >> Edge(color=PA_GRAY_D, style="dotted", label="no route")
                >> external
            )

        # The single most important edge in the figure is the one that is cut.
        (
            model
            >> Edge(
                color="#000000",
                style="dashed",
                label="no route exists during a procedure",
            )
            >> boundary
        )


if __name__ == "__main__":
    build()
