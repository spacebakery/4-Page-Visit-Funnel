from script import all_data


def funnel_ratio(col_n, df=all_data):
    try:
        if 1 < col_n < 5:
            dict_ = {1:'visit', 2:'cart', 3:'checkout', 4:'purchase'}
            str_col_1 = df.columns[(col_n - 1)]
            str_col_2 = df.columns[col_n]

            n_col_1 = len(df[str_col_1]) - df[str_col_1].isna().sum()
            n_col_2 = len(df[str_col_2]) - df[str_col_2].isna().sum()
            percentage = round((100 * (n_col_1 - n_col_2) / n_col_1), 2)

            message = '% of user who get to {} but did not get {}: {}'
            return message.format(dict_[col_n - 1], dict_[col_n], percentage)
        else:
            print('<Error: column level out of range>')
    except TypeError as error:    # if level (col_n) prompted is not valid type.
        print(error)
        print('<Invalid type --> Prompt an integer>')
    except TypeError:

