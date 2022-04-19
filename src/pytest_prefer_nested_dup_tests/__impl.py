import pytest
import _pytest.config
import _pytest.fixtures
from typing import (
    cast,
    Dict,
    List,
    Optional,
)


class ExtendedItem(pytest.Item):
    prefer_nested_dup_tests__parent_depth: int


def pytest_configure(config: _pytest.config.Config) -> None:
    config.option.keepduplicates = True


def pytest_collection_modifyitems(
    session: pytest.Session,
    config: _pytest.config.Config,
    items: List[ExtendedItem],
) -> None:
    session = session  # ignore unused var warning

    seen_best_nodes: Dict[str, ExtendedItem] = {}

    for item in items:
        item.prefer_nested_dup_tests__parent_depth = 0
        parent: Optional[ExtendedItem] = cast(Optional[ExtendedItem], item.parent)
        while parent != None:
            parent = cast(ExtendedItem, parent)
            item.prefer_nested_dup_tests__parent_depth = (
                item.prefer_nested_dup_tests__parent_depth + 1
            )
            parent = cast(Optional[ExtendedItem], parent.parent)
        if item.nodeid not in seen_best_nodes.keys():
            seen_best_nodes[item.nodeid] = item
        else:
            if (
                item.prefer_nested_dup_tests__parent_depth
                > seen_best_nodes[item.nodeid].prefer_nested_dup_tests__parent_depth
            ):
                seen_best_nodes[item.nodeid] = item

    new_items = list(seen_best_nodes.values())

    items[:] = new_items

    # fix how many items we report in terminal output b/c we do not "deselect" our removed duplicates (intentionally)
    terminal_plugin = config.pluginmanager.get_plugin("terminalreporter")
    terminal_plugin._numcollected = len(items)
    terminal_plugin.report_collect()
