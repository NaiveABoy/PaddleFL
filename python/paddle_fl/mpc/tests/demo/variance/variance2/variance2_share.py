import numpy as np
from paddle_fl.mpc.data_utils.data_utils import get_datautils

aby3 = get_datautils('aby3')

if __name__ == '__main__':
        with open(r'Input-P0.list', 'r') as file:
            content_list_0 = file.readlines()
        contentall_0 = [float(x) for x in content_list_0]
        avg_0 = np.mean(contentall_0)
        variance_0 = np.var(contentall_0, ddof = 1)

        data_1 = np.full((1), fill_value=avg_0)
        data_2 = np.full((1), fill_value=variance_0)
        data_1_shares = aby3.make_shares(data_1)
        data_2_shares = aby3.make_shares(data_2)
        data_1_all3shares = np.array([aby3.get_shares(data_1_shares, i) for i in range(3)])
        data_2_all3shares = np.array([aby3.get_shares(data_2_shares, i) for i in range(3)])
        np.save('data_C0_P0_avg.npy', data_1_all3shares[0])
        np.save('data_C0_P0_variance.npy', data_2_all3shares[0])
        np.save('data_C1_P0_avg.npy', data_1_all3shares[1])
        np.save('data_C1_P0_variance.npy', data_2_all3shares[1])
        np.save('data_C2_P0_avg.npy', data_1_all3shares[2])
        np.save('data_C2_P0_variance.npy', data_2_all3shares[2])

        with open(r'Input-P1.list', 'r') as file:
            content_list_1 = file.readlines()
        contentall_1 = [float(x) for x in content_list_1]
        avg_1 = np.mean(contentall_1)
        variance_1 = np.var(contentall_1, ddof=1)

        data_3 = np.full((1), fill_value=avg_1)
        data_4 = np.full((1), fill_value=variance_1)
        data_3_shares = aby3.make_shares(data_3)
        data_4_shares = aby3.make_shares(data_4)
        data_3_all3shares = np.array([aby3.get_shares(data_3_shares, i) for i in range(3)])
        data_4_all3shares = np.array([aby3.get_shares(data_4_shares, i) for i in range(3)])
        np.save('data_C0_P1_avg.npy', data_3_all3shares[0])
        np.save('data_C0_P1_variance.npy', data_4_all3shares[0])
        np.save('data_C1_P1_avg.npy', data_3_all3shares[1])
        np.save('data_C1_P1_variance.npy', data_4_all3shares[1])
        np.save('data_C2_P1_avg.npy', data_3_all3shares[2])
        np.save('data_C2_P1_variance.npy', data_4_all3shares[2])
        
        num_0 = 9
        num_1 = 10
        data_tmp = np.array([1/(num_0+num_1), num_0, num_1, num_0-1, num_1-1, 1/(num_0+num_1-1)])
        data_tmp_shares = aby3.make_shares(data_tmp)
        data_tmp_all3shares = np.array([aby3.get_shares(data_tmp_shares, i) for i in range(3)])
        np.save('data_C0_tmp.npy', data_tmp_all3shares[0])
        np.save('data_C1_tmp.npy', data_tmp_all3shares[1])
        np.save('data_C2_tmp.npy', data_tmp_all3shares[2])

        contentall = np.append(contentall_0,contentall_1)
        variance2 = np.var(contentall, ddof = 1)
        print(variance2)

