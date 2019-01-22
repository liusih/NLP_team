def spilt_data():
    all_data =pd.read_csv('all_data.tsv', sep='\t')

    #将样本分为x表示特征，y表示类别
    x,y = all_data.ix[:,1:],all_data.ix[:,0]
    #测试集为20%，训练集为80%
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
    print(x_train[0])
    print(len(x_train))
    print(len(x_test))



spilt_data()