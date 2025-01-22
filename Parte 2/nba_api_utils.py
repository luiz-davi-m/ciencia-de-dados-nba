def salvar_dataset_csv(data_set, path):
    data_set.to_csv(path, index=False)