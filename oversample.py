from imblearn.over_sampling import SMOTE, BorderlineSMOTE, ADASYN

class Oversample:

    @staticmethod
    def oversample(X_train_2d, Y_train, vul_type):

        print(vul_type)


        if vul_type == "CWE113" or vul_type == "CWE190" or vul_type == "CWE191" or vul_type == "CWE197" or vul_type == "CWE470"\
              or vul_type == "CWE476" or vul_type == "CWE506" or vul_type == "CWE606" or vul_type == "CWE690"\
                or vul_type == "CWE80" or vul_type == "CWE90":

            osp = SMOTE()
               
        elif vul_type == "CWE129" or vul_type == "CWE134" or vul_type == "CWE23" or vul_type == "CWE259" or vul_type == "CWE369"\
              or vul_type == "CWE400" or vul_type == "CWE601" or vul_type == "CWE643" or vul_type == "CWE81":
            osp = BorderlineSMOTE()

        else:
            osp = ADASYN()


        X_train_2d_resampled, Y_resampled = osp.fit_resample(X_train_2d, Y_train)


        Y_resampled = Y_resampled.reshape(-1, 1)

        return X_train_2d_resampled, Y_resampled

        

        