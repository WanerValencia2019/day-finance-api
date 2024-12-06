import importlib
from logging.config import fileConfig
import os
import pkgutil

from sqlalchemy import create_engine
from sqlalchemy import pool

from app.core.database.postgresql.connection import Base, SQLALCHEMY_DATABASE_URL

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# Ruta donde se encuentran los modelos
MODELS_PATH = "app"

# # Función para importar dinámicamente
# def import_all_models():
#     for module_info in pkgutil.walk_packages([os.path.join(os.getcwd(), MODELS_PATH)]):
#         if module_info.ispkg:
#             continue
#         module_name = f"{MODELS_PATH}.{module_info.name}"
#         print(f"Importing module: {module_name}")
#         importlib.import_module(module_name)
# import_all_models()

from app.users.infrastructure.models.user_model import UserAlchemyModel
from app.transactions.infrastructure.models.transaction_model import TransactionAlchemyModel
from app.transactions.infrastructure.models.category_model import CategoryAlchemyModel

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = SQLALCHEMY_DATABASE_URL
    print(f"SQLALCHEMY_DATABASE_URL: {url}")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()