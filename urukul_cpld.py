from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform
from migen.build.xilinx.ise import XilinxISEToolchain

_io = [
        ("tp", 0, Pins("P143"), Misc("SLEW=FAST")),
        ("tp", 1, Pins("P140"), Misc("SLEW=FAST")),
        ("tp", 2, Pins("P138"), Misc("SLEW=FAST")),
        ("tp", 3, Pins("P136"), Misc("SLEW=FAST")),
        ("tp", 4, Pins("P134"), Misc("SLEW=FAST")),

        ("ifc_mode", 0,
            Pins("P104 P105 P110 P111"),
            Misc("PULLUP")),

        ("clk", 0,
            Subsignal("div", Pins("P11"), Misc("SLEW=SLOW")),
            Subsignal("in_sel", Pins("P12"), Misc("SLEW=SLOW"))),

        ("att", 0,
            Subsignal("clk", Pins("P95"), Misc("SLEW=FAST")),
            Subsignal("le", Pins("P94"), Misc("SLEW=FAST")),
            Subsignal("rst_n", Pins("P96"), Misc("SLEW=SLOW")),
            Subsignal("s_in", Pins("P133"), Misc("SLEW=SLOW")),
            Subsignal("s_out", Pins("P97"), Misc("SLEW=FAST"))),

        ("dds_common", 0,
            Subsignal("master_reset", Pins("P102"), Misc("SLEW=SLOW")),
            Subsignal("reset", Pins("P120"), Misc("SLEW=SLOW")),
            Subsignal("io_reset", Pins("P129"), Misc("SLEW=SLOW")),
            Subsignal("profile", Pins("P130 P131 P132"), Misc("SLEW=FAST"))),

        ("dds_sync", 0,
            Subsignal("clk0", Pins("P38"),
                Misc("PULLUP")),  # DDS_SYNC_CLK0
            Subsignal("clk_out_en", Pins("P86")),  # DDS_SYNC_CLK_OUTEN
            Subsignal("sync_sel", Pins("P60")),  # DDS_SYNC_CLKSEL
            Subsignal("sync_out_en", Pins("P92"))),  # DDS_SYNC_OUTEN

        ("dds", 0,
            Subsignal("rf_sw", Pins("P103"), Misc("SLEW=FAST")),
            Subsignal("led", Pins("P128 P126"), Misc("SLEW=SLOW")),
            Subsignal("smp_err", Pins("P19"), Misc("PULLUP")),
            Subsignal("pll_lock", Pins("P21"), Misc("PULLUP")),
            Subsignal("io_update", Pins("P4"), Misc("SLEW=SLOW")),
            Subsignal("sck", Pins("P3"), Misc("SLEW=FAST")),
            Subsignal("sdo", Pins("P113"), Misc("SLEW=SLOW")),
            Subsignal("sdi", Pins("P2"), Misc("PULLUP")),
            Subsignal("cs_n", Pins("P119"), Misc("SLEW=SLOW"))),

        ("dds", 1,
            Subsignal("rf_sw", Pins("P101"), Misc("SLEW=FAST")),
            Subsignal("led", Pins("P118 P125"), Misc("SLEW=SLOW")),
            Subsignal("smp_err", Pins("P28"), Misc("PULLUP")),
            Subsignal("pll_lock", Pins("P35"), Misc("PULLUP")),
            Subsignal("io_update", Pins("P10"), Misc("SLEW=FAST")),
            Subsignal("sck", Pins("P9"), Misc("SLEW=FAST")),
            Subsignal("sdo", Pins("P6"), Misc("SLEW=SLOW")),
            Subsignal("sdi", Pins("P7"), Misc("PULLUP")),
            Subsignal("cs_n", Pins("P5"), Misc("SLEW=SLOW")),
        ),

        ("dds", 2,
            Subsignal("rf_sw", Pins("P100"), Misc("SLEW=FAST")),
            Subsignal("led", Pins("P116 P117")),
            Subsignal("smp_err", Pins("P40"), Misc("PULLUP")),
            Subsignal("pll_lock", Pins("P41"), Misc("PULLUP")),
            Subsignal("io_update", Pins("P14")),
            Subsignal("sck", Pins("P13"), Misc("SLEW=FAST")),
            Subsignal("sdo", Pins("P17"), Misc("SLEW=SLOW")),
            Subsignal("sdi", Pins("P15"), Misc("PULLUP")),
            Subsignal("cs_n", Pins("P16"), Misc("SLEW=SLOW"))),

        ("dds", 3,
            Subsignal("rf_sw", Pins("P98"), Misc("SLEW=FAST")),
            Subsignal("led", Pins("P121 P124"), Misc("SLEW=SLOW")),
            Subsignal("smp_err", Pins("P39"), Misc("PULLUP")),
            Subsignal("pll_lock", Pins("P49"), Misc("PULLUP")),
            Subsignal("io_update", Pins("P25"), Misc("SLEW=SLOW")),
            Subsignal("sck", Pins("P22"), Misc("SLEW=FAST")),
            Subsignal("sdo", Pins("P23"), Misc("SLEW=SLOW")),
            Subsignal("sdi", Pins("P26"), Misc("PULLUP")),
            Subsignal("cs_n", Pins("P24"), Misc("SLEW=SLOW"))),

        ("eem", 0,
            Subsignal("io", Pins("P30")),
            Subsignal("oe", Pins("P58"))),
        ("eem", 1,
            Subsignal("io", Pins("P53")),
            Subsignal("oe", Pins("P52"))),
        ("eem", 2,
            Subsignal("io", Pins("P45")),
            Subsignal("oe", Pins("P57"))),
        ("eem", 3,
            Subsignal("io", Pins("P50")),
            Subsignal("oe", Pins("P61"))),
        ("eem", 4,
            Subsignal("io", Pins("P43")),
            Subsignal("oe", Pins("P64"))),
        ("eem", 5,
            Subsignal("io", Pins("P51")),
            Subsignal("oe", Pins("P59"))),
        ("eem", 6,
            Subsignal("io", Pins("P54")),
            Subsignal("oe", Pins("P68"))),
        ("eem", 7,
            Subsignal("io", Pins("P56")),
            Subsignal("oe", Pins("P69"))),
        ("eem", 8,
            Subsignal("io", Pins("P32")),
            Subsignal("oe", Pins("P80"))),
        ("eem", 9,
            Subsignal("io", Pins("P71")),
            Subsignal("oe", Pins("P85"))),
        ("eem", 10,
            Subsignal("io", Pins("P74")),
            Subsignal("oe", Pins("P82"))),
        ("eem", 11,
            Subsignal("io", Pins("P78")),
            Subsignal("oe", Pins("P77"))),
        ("eem", 12,
            Subsignal("io", Pins("P70")),
            Subsignal("oe", Pins("P79"))),
        ("eem", 13,
            Subsignal("io", Pins("P87")),
            Subsignal("oe", Pins("P81"))),
        ("eem", 14,
            Subsignal("io", Pins("P76")),
            Subsignal("oe", Pins("P91"))),
        ("eem", 15,
            Subsignal("io", Pins("P88")),
            Subsignal("oe", Pins("P83"))),
]


class Platform(XilinxPlatform):
    def __init__(self):
        XilinxPlatform.__init__(self, "xc2c128-6-tq144", _io)
        self.toolchain.xst_opt = "-ifmt MIXED"
        self.toolchain.par_opt = ("-optimize speed -unused pullup "
                "-iostd LVCMOS33")
