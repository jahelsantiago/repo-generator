import tomli

with open("settings.toml", mode="rb") as fp:
     config = tomli.load(fp)