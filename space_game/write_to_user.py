def display_inventory(
    *, has_sufficient_credits: bool, has_hyperdrive_engine: bool, has_copilot: bool
) -> None:
    print("-" * 79)
    inventory = "\nYou have: "
    inventory += "plenty of credits, " if has_sufficient_credits else ""
    inventory += "a hyperdrive, " if has_hyperdrive_engine else ""
    inventory += "a skilled copilot, " if has_copilot else ""
    if inventory.endswith(", "):
        print(inventory.strip(", "))
