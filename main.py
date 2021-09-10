# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    from allure_behave.hooks import allure_report
    from behave.__main__ import main as behave_main

    behave_main("/Users/tehaseenmujawar/PycharmProjects/BDDFirstProject/features")


    ### your code

    allure_report("reports/")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
