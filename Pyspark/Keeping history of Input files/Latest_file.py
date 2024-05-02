from transforms.api import transform, Input, Output
import logging

logger = logging.getLogger(__name__)


@transform(
    output=Output("latest_file"),
    history=Input("history"),
)
def compute(history, output):

    fs = history.filesystem()
    csv_list = list(fs.ls())

    csv_list_name = sorted([csv.path for csv in csv_list], reverse=True)

    last_csv_file_name = csv_list_name[0]

    with history.filesystem().open(last_csv_file_name, 'r') as f:
        txt_content = f.read()

    logger.info(f"latest active PO file in: {last_csv_file_name}")

    with output.filesystem().open('latest_active_PO_ITA.csv', 'w') as f:
        f.write(txt_content)
