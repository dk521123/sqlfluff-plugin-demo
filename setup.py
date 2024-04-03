"""Setup file for an example rules plugin."""

from setuptools import find_packages, setup

PLUGIN_LOGICAL_NAME = "demo"
PLUGIN_ROOT_MODULE = "sqlfluff_plugin_demo"

setup(
  name=f"sqlfluff-plugin-{PLUGIN_LOGICAL_NAME}",
  url="https://dk521123.hatenablog.com/entry/2024/03/31/232907",
  license="MIT",
  description="This is just a sample",
  version="0.0.1",
  include_package_data=True,
  package_dir={"": "src"},
  packages=find_packages(where="src"),
  install_requires="sqlfluff>=0.4.0",
  entry_points={
    "sqlfluff": [
      f"sqlfluff_{PLUGIN_LOGICAL_NAME} = {PLUGIN_ROOT_MODULE}"
    ]
  },
)
