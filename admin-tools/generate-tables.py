#!/usr/bin/env python3
import csv

def string_from_codes(codes):
    """Generate a unicode string from a list of code points"""
    return "".join(chr(int(c[2:], 16)) for c in codes.split(" ") if c)

def unicode_url_from_code(code):
    return "https://www.compart.com/en/unicode/U+" + f"{int(wl_code[2:], 16):X}".zfill(4)

with open("resources/named-characters-data.csv", "r") as i, open("docs/translation-tables/full-unicode-conversion-table.rst", "w") as o:
    reader = csv.reader(i, delimiter=",", quotechar="|")
    header = next(reader)

    # The rows formatted in RST
    rst_rows = ["   * - " +  "\n     - ".join(header)]

    for row in reader:
        named, uni_name, wl_name, uni_code, wl_code, esc = row

        uni_code, wl_code = uni_code.strip(), wl_code.strip()
        esc = esc.replace("`", "\\`")

        named_url = f"https://reference.wolfram.com/language/ref/{named[2:-1]}.html"
        named = named.replace("\\", "\\\\")

        if uni_code:
            uni_code_rst = " ".join(f"`{c} <{unicode_url_from_code(c)}>`_" 
                                    for c in uni_code.split(" ")) 
            uni_code_rst += " \\" + string_from_codes(uni_code)
        
        parts = [f"   * - `{named} <{named_url}>`_", uni_name, wl_name, 
                uni_code_rst if uni_code else "",
                f"`{wl_code} <{unicode_url_from_code(wl_code)}>`_", 
                f"``{esc}``" if esc else "",]
        rst_row = "\n     - ".join(parts)
        rst_rows.append(rst_row)

    o.write(".. list-table Title\n")
    o.write("   :widths 20, 25, 25, 10, 10, 10\n")
    o.write("   :header-rows 1\n")
    o.write("\n\n\n")
    o.write("\n".join(rst_rows))



