"""Figure 17. The room you are in, the cabinet next to it, and the cable that is absent.

Type
    Diagrams (Python)-type, deployment architecture. Full-page figure.

Paper section
    Section 7, What Happens in the Operating Room.

Patient concern answered
    ChatGPT concern 11 (cybersecurity and network dependence), concern 2 (who is
    actually controlling the operation), and concern 10 (privacy and recording);
    Gemini family 4. The reassurance "it runs on premises" is worth nothing
    unless the reader can see the boundary. This figure draws the boundary, the
    three things that cross it before the procedure, and the nothing that
    crosses it during the procedure.

Why this diagram type
    A deployment diagram is the only construct in the permitted set that
    distinguishes a process from the machine it runs on and a machine from the
    network it sits on. The claim being made is about machines and networks, so
    the notation has to be about machines and networks.

Distinguished from the NSCLC journey
    The stack topology is adapted from the author's autonomous single-patient
    journey, which was non-small cell lung cancer. This deployment is PDAC: an
    eight-arm pancreaticoduodenectomy rather than a four-arm lobectomy, three
    anastomoses rather than one bronchial closure, and a vascular exclusion
    envelope around the superior mesenteric and portal veins that the thoracic
    configuration has no equivalent of.

TikZ rendering notes for full-patient
    Draw with the dg* vocabulary of patientstyle.sty. Full-page figure.
    Five dgcluster containers stacked as two columns:
      left column, x centre -4.6: sterile_field at y 0, or_support at y -6.4;
      right column, x centre 4.8: cabinet at y 0, evidence at y -6.4;
      full-width, y -12.2: boundary.
    Cluster inner sep 7pt; 1.8 cm of clear space between adjacent clusters.
    Every node is a \\dgnode / \\dgnodew / \\dgnodeg call: a 9 mm rounded tile
    carrying a vector pictogram with a \\tiny\\sffamily label beneath. Tile pitch
    2.5 cm horizontal, 2.3 cm vertical.
    Pictograms: \\glyphrobot for the arms, \\glyphsignal for the sensor bus,
    \\glyphmon for the console, \\glyphai for the model, \\glyphshield for the
    gate, \\glyphdb for the registry and the vault, \\glyphlock for the audit
    chain, \\glyphstop for the emergency stop, \\glyphnet for the boundary,
    \\glyphcloud for the outside world, \\glyphuser for the team roles.
    The absent cable is drawn as a dgedged dashed line from the cabinet cluster
    to the outside-world tile, interrupted at its midpoint by a 4 mm protoblack
    cross, with the label set in a white-filled node above the cross so nothing
    overlaps.
    Cross-cluster edges use to[out=0,in=180,looseness=0.85]; the two that must
    travel down a column use to[out=-90,in=90,looseness=0.75].
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
    "fontsize": "13",
    "bgcolor": PROTO_WHITE,
    "pad": "0.5",
    "nodesep": "1.0",
    "ranksep": "1.3",
    "compound": "true",
}

NODE_ATTR = {"fontname": "Helvetica", "fontsize": "10", "fontcolor": "#111111"}
EDGE_ATTR = {"fontname": "Helvetica", "fontsize": "9", "color": PROTO_GRAY}

# Protocol-specified limits, printed on the tiles they belong to so the figure
# carries its own evidence rather than deferring to the body text.
LIMITS = {
    "heartbeat_hz": 10_000,
    "estop_cross_arm_ms": 3,
    "estop_system_ms": 500,
    "tip_force_per_arm_n": 3.0,
    "tip_force_cumulative_n": 18.0,
    "positional_tolerance_mm": 2.0,
    "force_tolerance_n": 0.5,
    "sensor_channels": 640,
    "arms": 8,
}


def build() -> None:
    """Render the figure. No-op when mingrammer/diagrams is not installed."""
    try:
        from diagrams import Cluster, Diagram, Edge
        from diagrams.generic.compute import Rack
        from diagrams.generic.device import Tablet
        from diagrams.generic.network import Firewall, Router, Switch
        from diagrams.generic.storage import Storage
        from diagrams.programming.flowchart import Decision, Document, InputOutput
    except ImportError:
        return

    with Diagram(
        "Figure 17. Operating room and on-premises stack, with the boundary shown",
        filename="fig_17_operating_room_stack",
        show=False,
        direction="TB",
        outformat="svg",
        graph_attr=GRAPH_ATTR,
        node_attr=NODE_ATTR,
        edge_attr=EDGE_ATTR,
    ):
        with Cluster(
            "Sterile field, the table you are on", graph_attr={"bgcolor": PA_BLUE_2}
        ):
            arms = Rack(
                f"{LIMITS['arms']} robotic arms\n"
                f"tip force <= {LIMITS['tip_force_per_arm_n']} N each\n"
                f"<= {LIMITS['tip_force_cumulative_n']} N summed"
            )
            sensors = InputOutput(
                f"Sensor stack\n{LIMITS['sensor_channels']} channels\n"
                f"{LIMITS['heartbeat_hz'] // 1000} kHz heartbeat"
            )
            estop = Decision(
                f"Emergency stop\n<= {LIMITS['estop_cross_arm_ms']} ms cross-arm\n"
                f"<= {LIMITS['estop_system_ms']} ms system-wide"
            )
            sensors >> Edge(color=PROTO_GRAY, label="field state") >> arms
            estop >> Edge(color=PROTO_BLACK, label="halt, unconditional") >> arms

        with Cluster(
            "Operating room, non-sterile side", graph_attr={"bgcolor": PA_GRAY_L}
        ):
            console = Tablet("Surgeon console\nsole approval authority")
            second = Tablet("Second operator station\nindependent stop button")
            ism = Document("Independent safety monitor\npresent for every procedure")
            console >> Edge(color=PROTO_BLUE, label="signed motion command") >> arms
            second >> Edge(color=PROTO_BLACK, style="dashed", label="may stop") >> estop
            ism >> Edge(color=PROTO_BLACK, style="dashed", label="may stop") >> estop

        with Cluster(
            "On-premises cabinet, same building", graph_attr={"bgcolor": PA_GRAY_L}
        ):
            model = Rack("On-premises LLM\nadvisory only\nno actuator path")
            gate = Decision(
                f"Deterministic safety gate\npositional <= {LIMITS['positional_tolerance_mm']} mm\n"
                f"force <= {LIMITS['force_tolerance_n']} N"
            )
            registry = Storage("Version registry\nfrozen at your consent")
            sensors >> Edge(color=PROTO_GRAY) >> model
            (
                model
                >> Edge(color=PROTO_GRAY, style="dashed", label="candidate plan")
                >> gate
            )
            gate >> Edge(color=PROTO_BLUE, label="only passed plans") >> console
            registry >> Edge(color=PROTO_GRAY, label="pinned build") >> model

        with Cluster(
            "Evidence, written once and never edited", graph_attr={"bgcolor": PA_GRAY_L}
        ):
            audit = Storage(
                "Hash-chained audit trail\n21 CFR part 11\nseed and commit bound"
            )
            vault = Storage("Data vault\naccess list published to you")
            report = Document("Your day-30 and day-90\nresults, returned directly")
            gate >> Edge(color=PROTO_GRAY) >> audit
            console >> Edge(color=PROTO_GRAY) >> audit
            audit >> Edge(color=PROTO_GRAY) >> vault
            vault >> Edge(color=PROTO_BLUE) >> report

        with Cluster("Outside the building", graph_attr={"bgcolor": PA_GRAY_M}):
            boundary = Firewall("Network boundary\nclosed for the whole procedure")
            router = Router("Hospital network")
            cloud = Switch("Vendor support, cloud,\nremote assistance")
            boundary >> Edge(color=PA_GRAY_D, style="dotted") >> router
            router >> Edge(color=PA_GRAY_D, style="dotted") >> cloud

        # Three things cross the boundary, all of them before the procedure.
        (
            boundary
            >> Edge(
                color=PROTO_GRAY, style="dashed", label="before: signed model build"
            )
            >> registry
        )
        (
            boundary
            >> Edge(color=PROTO_GRAY, style="dashed", label="before: protocol version")
            >> gate
        )
        (
            audit
            >> Edge(
                color=PROTO_GRAY, style="dashed", label="after: reports to FDA and IRB"
            )
            >> boundary
        )

        # And one thing does not, which is the argument of the figure.
        (
            model
            >> Edge(
                color=PROTO_BLACK,
                style="dashed",
                label="DURING the procedure: no route exists",
            )
            >> boundary
        )


if __name__ == "__main__":
    build()
