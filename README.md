# Objective
* This is a demo for SQLFluff's custom rules

# How to install this SQLFluff plugin
```sh
# Install SQLFluff
pip install sqlfluff

# Install this custom rule
pip install git+https://github.com/dk521123/sqlfluff-plugin-demo.git

# To confirm
pip list | grep sqlfluff
```
## How to run
```sh
# sqlfluff lint --dialect <your-target-db><target_sql>
$ sqlfluff lint --dialect snowflake test.sql
== [test.sql] FAIL
L:   2 | P:  38 | Demo_L001 | Column `bar` not allowed in ORDER BY.
L:   5 | P:  38 | Demo_L001 | Column `bar` not allowed in ORDER BY.
All Finished !
```

## Uninstall
```sh
pip uninstall --yes sqlfluff-plugin-demo
```

# How to create Python packages
```sh
# Step1: Install build package
python -m pip install build

# Step2: create package
python -m build
```

# Links
## Official site
**Homepage**  
* https://docs.sqlfluff.com/en/stable/

**document**  
* https://docs.sqlfluff.com/en/stable/developingplugins.html
* https://github.com/sqlfluff/sqlfluff/tree/main/plugins/sqlfluff-plugin-example

## Others
* https://medium.com/sprocket-inc/sqlfluff%E3%81%AE%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0%E3%83%AB%E3%83%BC%E3%83%AB%E3%81%AE%E9%96%8B%E7%99%BA-f0d5ae7f5694
* https://github.com/hiroto3432/sqlfluff-plugin-custom
