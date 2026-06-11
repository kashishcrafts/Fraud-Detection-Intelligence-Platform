<<<<<<< HEAD
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    Float,
    DateTime
)

from datetime import datetime

DATABASE_URL = "postgresql://postgres:Cyber2026@localhost:5432/fraud_detection_db"
engine = create_engine(DATABASE_URL)

metadata = MetaData()

predictions_table = Table(
    "predictions",
    metadata,

    Column("id", Integer, primary_key=True),

    Column(
        "prediction",
        Integer,
        nullable=False
    ),

    Column(
        "fraud_probability",
        Float
    ),

    Column(
        "created_at",
        DateTime,
        default=datetime.utcnow
    )
)

metadata.create_all(engine)

=======
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    Float,
    DateTime
)

from datetime import datetime

DATABASE_URL = "postgresql://postgres:Cyber2026@localhost:5432/fraud_detection_db"
engine = create_engine(DATABASE_URL)

metadata = MetaData()

predictions_table = Table(
    "predictions",
    metadata,

    Column("id", Integer, primary_key=True),

    Column(
        "prediction",
        Integer,
        nullable=False
    ),

    Column(
        "fraud_probability",
        Float
    ),

    Column(
        "created_at",
        DateTime,
        default=datetime.utcnow
    )
)

metadata.create_all(engine)

>>>>>>> d7cc06efc5da1142cb42abd2819e93cfde5d83bb
print("Tables Created Successfully")