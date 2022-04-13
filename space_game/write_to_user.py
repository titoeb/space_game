def display_inventory(*, credits: bool, engines: bool, copilot: bool) -> None:
    print("-" * 79)
    inventory = "\nYou have: "
    inventory += "plenty of credits, " if credits else ""
    inventory += "a hyperdrive, " if engines else ""
    inventory += "a skilled copilot, " if copilot else ""
    if inventory.endswith(", "):
        print(inventory.strip(", "))
