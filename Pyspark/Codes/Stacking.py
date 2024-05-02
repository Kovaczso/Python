from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output


@transform_df(
    Output("Dataset"),
    bdda=Input("input1"),
    bdpa=Input("input2")
)
def compute(bdda,bdpa):

#BDPA DATES
    unpiv_dates = bdpa.select(
    F.expr("stack(120, 'PT001', PT001, 'PT002', PT002, 'PT003', PT003 ,'PT004', PT004 ,'PT005', PT005, 'PT006', PT006, 'PT007', PT007, 'PT008', PT008, 'PT009', PT009, 'PT010', PT010, 'PT011', PT011, 'PT012', PT012, 'PT013', PT013, 'PT014', PT014, 'PT015', PT015, 'PT016', PT016, 'PT017', PT017, 'PT018', PT018, 'PT019', PT019, 'PT020', PT020, 'PT021', PT021, 'PT022', PT022, 'PT023', PT023, 'PT024', PT024, 'PT025', PT025, 'PT026', PT026, 'PT027', PT027, 'PT028', PT028, 'PT029', PT029, 'PT030', PT030, 'PT031', PT031, 'PT032', PT032, 'PT033', PT033, 'PT034', PT034, 'PT035', PT035, 'PT036', PT036, 'PT037', PT037, 'PT038', PT038, 'PT039', PT039, 'PT040', PT040, 'PT041', PT041, 'PT042', PT042, 'PT043', PT043, 'PT044', PT044, 'PT045', PT045, 'PT046', PT046, 'PT047', PT047, 'PT048', PT048, 'PT049', PT049, 'PT050', PT050, 'PT051', PT051, 'PT052', PT052, 'PT053', PT053, 'PT054', PT054, 'PT055', PT055, 'PT056', PT056, 'PT057', PT057, 'PT058', PT058, 'PT059', PT059, 'PT060', PT060, 'PT061', PT061, 'PT062', PT062, 'PT063', PT063, 'PT064', PT064, 'PT065', PT065, 'PT066', PT066, 'PT067', PT067, 'PT068', PT068, 'PT069', PT069, 'PT070', PT070, 'PT071', PT071, 'PT072', PT072, 'PT073', PT073, 'PT074', PT074, 'PT075', PT075, 'PT076', PT076, 'PT077', PT077, 'PT078', PT078, 'PT079', PT079, 'PT080', PT080, 'PT081', PT081, 'PT082', PT082, 'PT083', PT083, 'PT084', PT084, 'PT085', PT085, 'PT086', PT086, 'PT087', PT087, 'PT088', PT088, 'PT089', PT089, 'PT090', PT090, 'PT091', PT091, 'PT092', PT092, 'PT093', PT093, 'PT094', PT094, 'PT095', PT095, 'PT096', PT096, 'PT097', PT097, 'PT098', PT098, 'PT099', PT099, 'PT100', PT100, 'PT101', PT101, 'PT102', PT102, 'PT103', PT103, 'PT104', PT104, 'PT105', PT105, 'PT106', PT106, 'PT107', PT107, 'PT108', PT108, 'PT109', PT109, 'PT110', PT110, 'PT111', PT111, 'PT112', PT112, 'PT113', PT113, 'PT114', PT114, 'PT115', PT115, 'PT116', PT116, 'PT117', PT117, 'PT118', PT118, 'PT119', PT119, 'PT120', PT120) as (date_cols, dates)")
 )
    unpiv_dates = unpiv_dates.withColumn('dates',F.to_timestamp(F.col('dates').cast('string'),'yyyyMMdd').cast('date'))
    unpiv_dates = unpiv_dates.withColumn('date_col_split',F.substring(F.col('date_cols'),-3,3))

#dem DF
    # Define the number of columns
    num_columns = 120

    # Generate column names and corresponding column values
    columns_and_values = []
    for i in range(1, num_columns + 1):
        column_name = f'BB{i:03d}'
        column_value = F.col(column_name)
        columns_and_values.extend([column_name, column_value])

    # Create the unpivoted DataFrame
    dem_df = bdda.select(
        F.col('BNR').alias('part'),
        F.col('BFL').alias('o_num'),
        F.col('BRT').alias('BRT'),
        F.expr(f"stack({num_columns}, " + ', '.join(f"'{col}', {val}" for col, val in zip(columns_and_values[::2], columns_and_values[0::2])) + f") as (COLS, qty)")
    )

    
    dem_df = (
        dem_df
            .withColumn('col_split',F.substring(F.col('COLS'),-3,3))
            .withColumn('type',F.lit('dem'))
            .withColumn('line',F.lit(None).cast('string'))
            .withColumn('loc2',F.lit('3'))
    )

    dem_df = dem_df.join(unpiv_dates,dem_df.col_split == unpiv_dates.date_col_split,'left')

    dem_df = dem_df.filter(F.col('qty') > 0)
    dem_df = dem_df.select(
        dem_df.o_num
        ,dem_df.BRT
        ,dem_df.line
        ,dem_df.qty
        ,dem_df.dates.alias('due_date')
        ,dem_df.type
        ,dem_df.loc2
        ,dem_df.part
        )

# NON_SERIAL dem

    # Define the number of columns
    num_columns = 120

    # Generate column names and corresponding column values
    columns_and_values = []
    for i in range(1, num_columns + 1):
        column_name = f'BDR{i:03d}'
        column_value = F.col(column_name)
        columns_and_values.extend([column_name, column_value])

    # Create the unpivoted DataFrame
    nonserial_df = bdda.select(
        F.col('BNR').alias('part'),
        F.lit('NONSERIAL').alias('o_num'),
        F.col('BRT').alias('BRT'),
        F.expr(f"stack({num_columns}, " + ', '.join(f"'{col}', {val}" for col, val in zip(columns_and_values[::2], columns_and_values[0::2])) + f") as (NON_COLS, qty)")
    )

    nonserial_df = (
        nonserial_df
            .withColumn('col_split',F.substring(F.col('NON_COLS'),-3,3))
            .withColumn('type',F.lit('dem'))
            .withColumn('line',F.lit(None).cast('string'))
            .withColumn('loc2',F.lit('3'))
    )

    nonserial_df = nonserial_df.join(unpiv_dates,nonserial_df.col_split == unpiv_dates.date_col_split,'left')

    nonserial_df = nonserial_df.filter(F.col('qty') > 0)
    nonserial_df = nonserial_df.select(
        nonserial_df.o_num
        ,nonserial_df.BRT
        ,nonserial_df.line
        ,nonserial_df.qty
        ,nonserial_df.dates.alias('due_date')
        ,nonserial_df.type
        ,nonserial_df.loc2
        ,nonserial_df.part
        )

# SUPPLY

    #Supply types
    
    # Define the number of columns
    num_columns = 120

    # Generate column names and corresponding column values
    columns_and_values = []
    for i in range(1, num_columns + 1):
        column_name = f'BDF{i:03d}'
        column_value = F.col(column_name)
        columns_and_values.extend([column_name, column_value])

    # Create the unpivoted DataFrame
    sup_types_df = bdda.select(
        F.col('BNR').alias('part'),
        F.col('BFL').alias('o_num'),
        F.col('BRT').alias('BRT'),
        F.expr(f"stack({num_columns}, " + ', '.join(f"'{col}', {val}" for col, val in zip(columns_and_values[::2], columns_and_values[0::2])) + f") as (SUP_TYPE_COL, supp_type)")
    )

    sup_types_df = (
        sup_types_df
            .withColumn('split',F.substring(F.col('SUP_TYPE_COL'),-3,3))
            .withColumn('type',
                F.when(F.col('supp_type') == '','SUPPLY')
                .when(F.col('supp_type').isin('P','?'),'SUPPLYP')
                .otherwise(F.col('supp_type'))
            )
    )
    cols_to_drop = ['part','o_num','BRT','SUP_TYPE_COL','supp_type']
    for cols in cols_to_drop:
        sup_types_df = sup_types_df.drop(cols)

    # Define the number of columns
    num_columns = 120

    # Generate column names and corresponding column values
    columns_and_values = []
    for i in range(1, num_columns + 1):
        column_name = f'BDO{i:03d}'
        column_value = F.col(column_name)
        columns_and_values.extend([column_name, column_value])

    # Create the unpivoted DataFrame
    supply_df = bdda.select(
        F.col('BNR').alias('part'),
        F.col('BFL').alias('o_num'),
        F.col('BRT').alias('BRT'),
        F.expr(f"stack({num_columns}, " + ', '.join(f"'{col}', {val}" for col, val in zip(columns_and_values[::2], columns_and_values[0::2])) + f") as (SUPPLY_COLS, qty)")
    )

    supply_df = (
        supply_df
            .withColumn('col_split',F.substring(F.col('SUPPLY_COLS'),-3,3))
            .withColumn('line',F.lit(None).cast('string'))
            .withColumn('loc2',F.lit('3'))
    )

    supply_df = supply_df.join(unpiv_dates,supply_df.col_split == unpiv_dates.date_col_split,'left')
    supply_df = supply_df.join(sup_types_df, sup_types_df.split == supply_df.col_split,'left')

    supply_df = supply_df.filter((F.col('qty') > 0) & (F.col('BRT').isin(2,3,9)))
    supply_df = supply_df.select(
        supply_df.o_num
        ,supply_df.BRT
        ,supply_df.line
        ,supply_df.qty
        ,supply_df.dates.alias('due_date')
        ,supply_df.type
        ,supply_df.loc2
        ,supply_df.part
        )

#  BDV SUPPLY

    # Define the number of columns
    num_columns = 120

    # Generate column names and corresponding column values
    columns_and_values = []
    for i in range(1, num_columns + 1):
        column_name = f'BDV{i:03d}'
        column_value = F.col(column_name)
        columns_and_values.extend([column_name, column_value])

    # Create the unpivoted DataFrame
    bdv_supply = bdda.select(
        F.col('BNR').alias('part'),
        F.col('BFL').alias('o_num'),
        F.col('BRT').alias('BRT'),
        F.expr(f"stack({num_columns}, " + ', '.join(f"'{col}', {val}" for col, val in zip(columns_and_values[::2], columns_and_values[0::2])) + f") as (bdv_cols, qty)")
    )

    bdv_supply = (
        bdv_supply
            .withColumn('col_split',F.substring(F.col('bdv_cols'),-3,3))
            .withColumn('type',F.lit('SUPPLY'))
            .withColumn('line',F.lit(None).cast('string'))
            .withColumn('loc2',F.lit('3'))
    )

    bdv_supply = bdv_supply.join(unpiv_dates,bdv_supply.col_split == unpiv_dates.date_col_split,'left')

    bdv_supply = bdv_supply.filter(
        (F.col('qty') > 0) & (F.col('BRT').isin(1,4)))
    bdv_supply = bdv_supply.select(
        bdv_supply.o_num
        ,bdv_supply.BRT
        ,bdv_supply.line
        ,bdv_supply.qty
        ,bdv_supply.dates.alias('due_date')
        ,bdv_supply.type
        ,bdv_supply.loc2
        ,bdv_supply.part
        )


    df_unioned = dem_df.unionByName(nonserial_df,allowMissingColumns= True)
    df_unioned = df_unioned.unionByName(supply_df,allowMissingColumns= True)
    df_unioned = df_unioned.unionByName(bdv_supply,allowMissingColumns= True) 

    df = (
        df_unioned
        .withColumn('part_key',F.lit(None).cast('string'))
        .withColumn('site_key',
                F.concat_ws('~',
                    F.lit('loc1')
                    ,F.col('loc2')
                    ,F.col('loc2')
                    ,F.col('part')
                )
            )
            .withColumn('site_key2',
                F.concat_ws('~',
                    F.lit('loc1')
                    ,F.col('loc2')
                    ,F.col('loc2')
                )
            )
    )

    return df
