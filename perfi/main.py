# file: main.py
# author: mbiokyle29
import logging

from click import argument, command, option, Path
from yaml import safe_load

from perfi.lib.asset import Asset, ReoccurringIncome
from perfi.lib.liability import Liability, ReoccurringCost
from perfi.utils import configure_logger, format_dollar_amount, format_percent, Every


root_logger = logging.getLogger("perfi")


@command()
@argument("personal_finances", nargs=1, type=Path(exists=True, resolve_path=True))
@option("-v", "--verbose", default=False, is_flag=True, help="Enable verbose logging.")
@option("-d", "--debug", default=False, is_flag=True, help="Enable debug logging.")
def cli(personal_finances, verbose, debug):
    configure_logger(root_logger, logging.INFO)
    root_logger.info("Starting perfi!")
    root_logger.info("Using personal finance data from %s", personal_finances)

    models_by_name = {
        Asset.__name__: Asset,
        Liability.__name__: Liability,
        ReoccurringCost.__name__: ReoccurringCost,
        ReoccurringIncome.__name__: ReoccurringIncome
    }

    raw_fin_data = {}
    raw_fin_data.update(safe_load(open(personal_finances)))

    holdings = {
        "assets": [],
        "liabilities": [],
        "reoccurring_costs": [],
        "reoccurring_incomes": []
    }

    # assets
    for key in ["assets", "liabilities", "reoccurring_costs", "reoccurring_incomes"]:

        for block in raw_fin_data.get(key, []):
            model_cls = models_by_name.get(block["model"])
            model_instance = model_cls.from_yaml(block)
            holdings[key].append(model_instance)

    root_logger.info(
        "Parsed %s assets and %s liabilities from personal data",
        len(holdings["assets"]),
        len(holdings["liabilities"]),
    )

    total_assets = sum([a.principal for a in holdings["assets"]])
    average_asset_apr = sum([a.apr for a in holdings["assets"]]) / max(len(holdings["assets"]), 1)

    total_liabilities = sum([a.principal for a in holdings["liabilities"]])
    average_liability_apr = sum([a.apr for a in holdings["liabilities"]]) / max(len(holdings["liabilities"]), 1)

    net_worth = total_assets - total_liabilities

    if len(holdings["assets"]) > 0:
        root_logger.info("ASSETS:")
        for asset in holdings["assets"]:
            root_logger.info(str(asset))

    root_logger.info(
        "You have a total of %s in assets with an average APR of %s",
        format_dollar_amount(total_assets),
        format_percent(average_asset_apr)
    )

    if len(holdings["liabilities"]) > 0:
        root_logger.info("LIABILITIES:")
        for liability in holdings["liabilities"]:
            root_logger.info(str(liability))

    root_logger.info(
        "You have a total of %s in liabilities with an average APR of %s",
        format_dollar_amount(total_liabilities),
        format_percent(average_liability_apr)
    )

    root_logger.info("Your net worth is: %s", format_dollar_amount(net_worth))

    total_montly_costs = sum([
        Every.convert_amount(
            cost_inst.every,
            Every.MONTH,
            cost_inst.cost
        )
        for cost_inst in holdings["reoccurring_costs"]
    ])

    total_montly_incomes = sum([
        Every.convert_amount(
            income_inst.every,
            Every.MONTH,
            income_inst.cost
        )
        for income_inst in holdings["reoccurring_incomes"]
    ])

    if len(holdings["reoccurring_costs"]) > 0:
        root_logger.info("REOCCURRING COSTS:")
        for cost_inst in holdings["reoccurring_costs"]:
            root_logger.info(str(cost_inst))

    root_logger.info("Your reoccurring costs (monthly): %s", format_dollar_amount(total_montly_costs))

    if len(holdings["reoccurring_incomes"]) > 0:
        root_logger.info("REOCCURRING INCOME:")
        for income_inst in holdings["reoccurring_incomes"]:
            root_logger.info(str(income_inst))

    root_logger.info("Your reoccurring income (monthly): %s", format_dollar_amount(total_montly_incomes))

    net_reoccurring = total_montly_incomes - total_montly_costs
    root_logger.info("Your net reoccurring balance (monthly): %s", format_dollar_amount(net_reoccurring))
