def main():
    spacecraft = {"name":"Voyager",
                  "distance":"163"}
    spacecraft.update({"orbit":"Sun"})
    print(create_report(spacecraft))
def create_report(spacecraft):
    return f"""
==========REPORT==========
Name:{spacecraft.get("name") }
Distance:{spacecraft["distance"]}
Orbit: {spacecraft["orbit"]}
==========================
"""
main()