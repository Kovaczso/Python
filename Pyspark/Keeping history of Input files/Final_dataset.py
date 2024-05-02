from transforms.api import transform, Input, Output
from pyspark.sql import functions as F

@transform(
    output=Output("output_dataset"),
    file=Input("latest_file"),
)
def compute(ctx, file, output):

    fs = file.filesystem()
    csv_list = list(fs.ls())

    for csv_file in csv_list:
        hadoop_path = fs.hadoop_path
        file_path = f"{hadoop_path}/{csv_file.path}"
        df = ctx.spark_session.read.csv(file_path, header=True, sep="|")

    # Rename columns
    renames = {
        "Col1": "part",
        "Col2": "po",
        "Col3": "line",
        "Col4": "supp",
        "Col5": "cust",
        "Col6": "add1",
        "Col7": "add2",
        "Col8": "phone",
        "Col9": "email",
    }

    for colname, rename in renames.items():
        df = df.withColumnRenamed(colname, rename)

    df = df.drop("_c9")

    output.write_dataframe(df)
