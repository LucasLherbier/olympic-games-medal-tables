import pandas as pd
import numpy as np

def preprocess_data(df, country_to_code, code_to_country):
    df = df.replace(0, np.NaN)
    return df.replace(country_to_code).replace(code_to_country).replace(country_to_code)


def read_table (data, filter = 'normal', function = lambda x :x) :
    """
    Display table as common ranking
    """
    df_table = pd.DataFrame()
    df = data.copy()
    #Get the rankings
    list_ranking = [i for i in df.columns if i.isdigit()] 
    # Build the new dataframe
    if filter not in df.columns : 
        exit(f'La colonne {filter} n est pas présente.')
    for i in list_ranking : 
        df_table = pd.concat([df_table, df.groupby([i])[filter].sum()], axis = 1)
    df_table.columns = list_ranking
    df_table = df_table.iloc[1:,:].fillna(0).round(0).astype('int64')

    return function(df_table)


def get_best(df, nb_max = None, top = 20, max_points = True) :
    # Get only the columns defined as medals
    df_table = df.iloc[:,:nb_max]
    df_table['total'] = df_table.sum(axis=1)
    df_tabl_col = [str(i) for i in df_table.columns][:-1]
    if max_points : 
        df_table['rank'] = df_table['total'].rank(ascending=False).astype('int64')
    else :
        df_table['rank'] = df_table.sort_values(df_tabl_col, ascending=False).groupby(df_tabl_col, sort=False).ngroup() + 1
    df_table = df_table.sort_values(['rank'], ascending=True)
    return df_table[:top].round(2)


def get_range(type, medals):
    if type =='successive' :
        return [i for i in range(medals,0, -1)]
    if type == 'proportional_by_2' :
        if medals > 8 :
            end_list = [i for i in range(medals-8,0, -1)]
            max_list = max(end_list)//2*2
            return [i for i in range(max_list+16,max_list, -2)]  + end_list
        else :
            return [i for i in range(medals*2,0, -2)]
    if type == 'proportional_by_5' :
        if medals > 8 :
            end_list = [i for i in range(medals-8,0, -1)]
            max_list = max(end_list)//5*5
            return [i for i in range(max_list+40,max_list, -5)]  + end_list
        else :
            return [i for i in range(medals*5,0, -5)]
    if type == 'proportional_by_10' :
        if medals > 8 :
            end_list = [i for i in range(medals-8,0, -1)]
            max_list = max(end_list)//10*10
            return [i for i in range(max_list+80,max_list, -10)]  + end_list
        else :
            return [i for i in range(medals*10,0, -10)]
    if type =='ski_points' :
        return [100,80,60,50,45,40,36,32,29,26,24,22,20,18,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1][:medals]
    if type =='biathlon_points' :
        return [60,54,48,43,40,38,36,34,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1][:medals]
    if type =='formula_one_points' :
        return [25,18,15,12,10,8,6,4,2,1][:medals]


def weighted_results_max(data,type_weights = 'successive', medals = 3, top = 10, filter = 'normal', function = lambda x : x) : 
    list_weights = get_range(type_weights, medals)
    new_data = read_table(data, filter, function)
    new_data = get_best(new_data, len(list_weights), top).iloc[:, :-2]*list_weights
    new_data['total'] = new_data.sum(axis=1)
    new_data = new_data.sort_values(['total'], ascending=False)
    new_data['rank'] = range(1, new_data.shape[0]+1)
    return new_data.round(2)



def merge_data(df1, df2) :
    nb_col_1 =  int(df1.columns[-1])
    nb_col_2 =  int(df2.columns[-1])
    if nb_col_2 > nb_col_1:
        df1[[str(i+1) for i in range (nb_col_1, nb_col_2)]] = 0
        return  df1.append(df2)
    else : 
        df2[[str(i+1) for i in range (nb_col_2, nb_col_1)]] = 0
        return df1.append(df2)

