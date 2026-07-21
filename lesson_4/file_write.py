with open("greeting.txt","w",encoding="utf-8") as file:
    file.write("Hello,automated tests!\n")
    file.write("second line")


def log_test_result(test_name,status):
    with open("test_run.txt","a",encoding="utf-8") as log_file:
        log_file.write(f'{test_name}: {status}\n')

log_test_result("test_login","success")
log_test_result("test_registration","fail")
log_test_result("test_logout","success")
