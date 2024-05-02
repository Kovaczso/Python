from transforms.api import transform, incremental, Input, Output
import datetime


@incremental(semantic_version=3)
@transform(
    output=Output("history"),
    uploads=Input("raw_inputs"),
)
def compute(uploads, output):

    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d_%Hh%Mm%Ss')

    fs = uploads.filesystem()
    csv_list = list(fs.ls())

    csv_content_dic = {}

    for csv_file in csv_list:

        csv_filenmane = csv_file.path

        with uploads.filesystem().open(csv_filenmane, 'r') as f:
            txt_content = f.read()

        csv_filenmane_extended = f"loaded_at_{now_str}___{csv_filenmane}"

        csv_content_dic[csv_filenmane_extended] = txt_content

    output.set_mode('modify')

    for csv_filenmane in csv_content_dic.keys():

        # results will be appended (incremental transform)
        with output.filesystem().open(csv_filenmane, 'w') as f:
            f.write(csv_content_dic[csv_filenmane])
