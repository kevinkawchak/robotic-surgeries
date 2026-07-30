"""Figure 30. After the last visit: who pays, who follows up, and what stays available.

Type
    Diagrams (Python)-type, lifecycle architecture spanning three time zones.

Paper section
    Section 12, Patient Rights, Costs, and H. R. 9510 v5.

Patient concern answered
    ChatGPT concern 16 (practical, financial, and post-trial burdens) and
    Gemini family 6 (increased costs). This is the concern that ranks high in
    prevalence and low in answer completeness on Figure 7, and the honest way to
    close a proponent's paper is to spend its last figure on the weakest part of
    the argument rather than the strongest.

Why this diagram type
    Cost and continuity are questions about which institution holds which
    obligation over which interval. That is an infrastructure question, not a
    process question, and a lifecycle architecture with three time-zone clusters
    is the construct that renders obligations as regions rather than as prose.

TikZ rendering notes for full-patient
    Draw with the dg* vocabulary of patientstyle.sty.
    Three dgcluster time zones left to right at x centres -6.2, 0.6, 7.6:
    "during the study", "the 12 months after your last visit", and "beyond".
    A fourth dgcluster2 payer container spans the full width at y -7.4.
    Every node is a \\dgnode call; tile pitch 2.4 cm horizontal, 2.3 cm
    vertical, giving at least 13 mm of clear space between tile edges.
    Pictograms: \\glyphflask for study procedures, \\glyphpill for the drug,
    \\glyphuser for clinician contact, \\glyphdoc for records, \\glyphdb for the
    data vault, \\glyphgear for device support, \\glyphchart for the cost table,
    \\glyphclock for each interval marker.
    Each cost tile carries a two-line label: the item, then who pays, in
    \\tiny\\sffamily\\itshape.
    Obligations that end are drawn with a 3 mm protoblack terminator bar at the
    boundary of their time zone, so an obligation that stops is visibly
    different from one that continues.
    Cross-zone edges use to[out=0,in=180,looseness=0.85]; payer edges rising
    from the payer container use to[out=90,in=-90,looseness=0.8].
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
    "nodesep": "0.9",
    "ranksep": "1.2",
}

NODE_ATTR = {"fontname": "Helvetica", "fontsize": "10", "fontcolor": "#111111"}
EDGE_ATTR = {"fontname": "Helvetica", "fontsize": "9", "color": PROTO_GRAY}

# Who pays for what. "sponsor" means no bill reaches the participant; "routine"
# means the participant's usual insurance arrangement applies exactly as it
# would outside the study; "open" means the answer is not yet settled and the
# paper says so rather than implying otherwise.
PAYER = {
    "investigational_drug": "sponsor",
    "robotic_platform_use": "sponsor",
    "study_only_imaging": "sponsor",
    "study_only_labs": "sponsor",
    "protocol_required_visits": "sponsor",
    "standard_surgical_care": "routine",
    "standard_inpatient_stay": "routine",
    "travel_and_lodging": "sponsor, capped",
    "lost_income": "open",
    "research_related_injury_care": "sponsor",
    "long_term_survivorship_care": "routine",
    "continued_drug_after_study": "open",
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
        "Figure 30. Post-trial continuity and who pays for each part of it",
        filename="fig_30_post_trial_continuity",
        show=False,
        direction="LR",
        outformat="svg",
        graph_attr=GRAPH_ATTR,
        node_attr=NODE_ATTR,
        edge_attr=EDGE_ATTR,
    ):
        with Cluster(
            "During the study, day -28 to month 24", graph_attr={"bgcolor": PA_BLUE_2}
        ):
            drug = InputOutput("Daraxonrasib\nsupplied by the sponsor")
            platform = Action("Robotic platform use\nno charge to you")
            visits = PredefinedProcess(
                "18 protocol visits\nsponsor pays study-only items"
            )
            injury = Document(
                "Research-related injury care\nsponsor pays, stated in consent"
            )
            drug >> Edge(color=PROTO_GRAY) >> visits
            platform >> Edge(color=PROTO_GRAY) >> visits
            visits >> Edge(color=PROTO_GRAY) >> injury

        with Cluster(
            "The 12 months after your last visit", graph_attr={"bgcolor": PA_GRAY_L}
        ):
            handback = Action("Care handed back to your\nown oncology team, in writing")
            records = Document("Full record copy to you\nand to your oncologist")
            device_support = Action("Device support obligation\nends at study closure")
            survivorship = PredefinedProcess(
                "Survivorship follow-up\non the routine pathway"
            )
            injury >> Edge(color=PROTO_BLUE, label="continues if related") >> handback
            handback >> Edge(color=PROTO_GRAY) >> records
            handback >> Edge(color=PROTO_GRAY) >> survivorship
            (
                visits
                >> Edge(color=PROTO_BLACK, style="dashed", label="ends")
                >> device_support
            )

        with Cluster(
            "Beyond, and what remains available", graph_attr={"bgcolor": PA_GRAY_M}
        ):
            vault = Storage("Your data, retrievable\non request, 15 years")
            results = Document(
                "Study results, sent to you\nwhether or not you completed"
            )
            continued = Action(
                "Continued access to the drug\nnot guaranteed by this protocol"
            )
            registry = Storage("Long-term safety registry\nvoluntary, separate consent")
            records >> Edge(color=PROTO_GRAY) >> vault
            survivorship >> Edge(color=PROTO_GRAY) >> results
            survivorship >> Edge(color=PROTO_GRAY, style="dashed") >> registry
            device_support >> Edge(color=PROTO_BLACK, style="dashed") >> continued

        with Cluster("Who pays", graph_attr={"bgcolor": PA_GRAY_L}):
            sponsor_pays = Document(
                "Sponsor\ndrug, platform, study-only\nimaging and labs, injury care,\ntravel to a cap"
            )
            routine_pays = Document(
                "Your usual arrangement\nstandard surgical care and\ninpatient stay, exactly as\noutside the study"
            )
            unsettled = Document(
                "Not settled by this protocol\nlost income, and continued\ndrug access after closure"
            )
            sponsor_pays >> Edge(color=PROTO_BLUE, style="dashed") >> drug
            sponsor_pays >> Edge(color=PROTO_BLUE, style="dashed") >> platform
            sponsor_pays >> Edge(color=PROTO_BLUE, style="dashed") >> injury
            routine_pays >> Edge(color=PROTO_GRAY, style="dashed") >> survivorship
            unsettled >> Edge(color=PROTO_BLACK, style="dashed") >> continued

        # The legislative proposal that would close the two unsettled items.
        (
            unsettled
            >> Edge(
                color=PROTO_BLUE,
                style="dotted",
                label="H. R. 9510 v5 would close both",
            )
            >> registry
        )


if __name__ == "__main__":
    build()
