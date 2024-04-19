from task1 import task1 as t1
from task2 import task2 as t2
from task3 import task3 as t3
from task4 import task4 as t4
from task5 import task5 as t5

if __name__ == "__main__":
    while True:
        input_choice = int(
            input(
                "\n---Choose task---\n"
                "-1: Task1\n"
                "-2: Task2\n"
                "-3: Task3\n"
                "-4: Task4\n"
                "-5: Task5\n"
                "-0: Exit\n"
            )
        )
        match input_choice:
            case 0:
                print("---Bye bye---")
                break
            case 1:
                t1.task1_run()
            case 2:
                t2.task2_run()
            case 3:
                t3.task3_run()
            case 4:
                t4.task4_run()
            case 5:
                t5.task5_run()
