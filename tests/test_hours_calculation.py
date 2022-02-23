from hours_calculating_functions import calculating_each_doctor_hours


def test_calculating_total_hours():
    (ari, gilat, emergency) = calculating_each_doctor_hours('C:\Users\user\Desktop\Excel data analysis\examples\1.20.xlsx',
                                                          18, 22)
    assert (ari, gilat, emergency) == (0.66666666666665, 81.00000000000001, 16.83333333333331)
