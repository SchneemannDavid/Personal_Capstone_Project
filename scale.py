from sklearn.preprocessing import MinMaxScaler, RobustScaler


### Scaling Functions ###

#-----------------------------------------------------------------------#

## Scaling ##

#Define function to scale all data based on the train subset
def minmax_scale_data(train, validate, test):
    
    scale_columns = ['bedrooms', 'bathrooms', 'garage_spaces', 'sq_ft']
    
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    mms = MinMaxScaler()
    
    mms.fit(train[scale_columns])
    
    train_scaled[scale_columns] = mms.transform(train[scale_columns])
    validate_scaled[scale_columns] = mms.transform(validate[scale_columns])
    test_scaled[scale_columns] = mms.transform(test[scale_columns])
    
    return train_scaled, validate_scaled, test_scaled


###

#Define function to scale all data based on the train subset
def robust_scale_data(train, validate, test):
    
    scale_columns = ['Distance']
    
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    rbs = RobustScaler()
    
    rbs.fit(train[scale_columns])
    
    train_scaled[scale_columns] = rbs.transform(train[scale_columns])
    validate_scaled[scale_columns] = rbs.transform(validate[scale_columns])
    test_scaled[scale_columns] = rbs.transform(test[scale_columns])
    
    return train_scaled, validate_scaled, test_scaled