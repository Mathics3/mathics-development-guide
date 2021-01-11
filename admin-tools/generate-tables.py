#!/usr/bin/env python3
import csv
import os
import os.path as osp

def get_srcdir():
    filename = osp.normcase(osp.dirname(osp.abspath(__file__)))
    return osp.realpath(filename)

os.chdir(get_srcdir() + "/../")

def format_code_points(codes: str, show_gliphs=False) -> str:
    codes = codes.strip()

    if not codes:
        return ""

    def unicode_url_from_code(c: str) -> str:
        return "https://www.compart.com/en/unicode/U+" + f"{int(c[2:], 16):X}".zfill(4)

    cs = codes.split(" ")
    output = " ".join(f"`{c} <{unicode_url_from_code(c)}>`_" for c in cs)

    if show_gliphs:
        output += " \\" + "".join(chr(int(c[2:], 16)) for c in cs)

    return output

def format_named_char(n: str) -> str:
    url = f"https://reference.wolfram.com/language/ref/character/{n[2:-1]}.html"

    return f"`\\{n} <{url}>`_"

def format_esc_sequence(seq: str) -> str:
    return "".join("\\" + c for c in seq.replace(" ", "␣"))

class TableWriter:
    def __init__(self, output, title, header, widths=None):
        if type(header) != list or (widths is not None and type(widths) != list):
            raise ValueError

        if not len(header):
            raise ValueError

        if type(widths) == list and len(widths) != len(header):
            raise ValueError

        self._o = output
        self._n_rows = len(header)

        self._o.write(f".. list-table:: {title}\n")

        if widths:
            self._o.write(
                "   :widths: " + ", ".join(str(w) for w in widths) + "\n"
            )

        self._o.write("   :header-rows: 1\n")
        self._o.write("\n\n\n")

        self.writerow(header)

    def writerow(self, row: list):
        if type(row) != list or len(row) != self._n_rows:
            raise ValueError(
                f"{repr(row)} is not a {self._n_rows} element list"
            )

        row_formated = ["   * - " + str(row[0])] + [str(c) for c in row[1:]]
        self._o.write("\n     - ".join(row_formated) + "\n")


# Generate the complete table
with open("resources/named-characters-data.csv", "r") as i, open("docs/translation-tables/full-unicode-conversion-table.rst", "w") as o:
    reader = csv.reader(i, delimiter=",", escapechar="|")
    next(reader) # Skip the header

    header = ["Named character", "Unicode", "WL", "ESC sequence alias"]
    writer = TableWriter(o, "Named characters data", header, [25, 35, 35, 15])

    for row in reader:
        named_char, _, _, uni, wl, esc = row

        writer.writerow([format_named_char(named_char),
                        format_code_points(uni, show_gliphs=True),
                        format_code_points(wl),
                        format_esc_sequence(esc)])


# Generate the Unicode to WL table
with open("resources/unicode-to-wl-conversion.csv", "r") as i, open("docs/translation-tables/unicode-to-wl-conversion-table.rst", "w") as o:
    reader = csv.reader(i, delimiter=",", escapechar="|")
    writer = TableWriter(o, "Unicode to WL conversions", next(reader),
                        [15, 35, 35, 25])

    for row in reader:
        uni_name, uni, wl, named_char = row

        writer.writerow([uni_name,
                        format_code_points(uni, show_gliphs=True),
                        format_code_points(wl),
                        format_named_char(named_char)])

# Generate the WL to Unicode table
with open("resources/wl-to-unicode-conversion.csv", "r") as i, open("docs/translation-tables/wl-to-unicode-conversion-table.rst", "w") as o:
    reader = csv.reader(i, delimiter=",", escapechar="|")
    writer = TableWriter(o, "WL to Unicode conversion", next(reader),
                        [25, 35, 35, 15])

    for row in reader:
        named_char, wl, uni, uni_name = row

        writer.writerow([format_named_char(named_char),
                        format_code_points(wl),
                        format_code_points(uni, show_gliphs=True),
                        uni_name])
