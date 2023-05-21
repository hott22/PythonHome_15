import logging
import argparse

FORMAT = '{msg}'
logging.basicConfig(style='{', filename='bank.log.',
                    filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

TAKE_OFF_TAX = 0.015
EVERY_THIRD_OPERATION_TAX = 0.03

WEALTH_TAX = 0.1
WEALTH = 5_000_000

START = 0

MIN_TAKE_OFF_TAX = 30
MAX_TAKE_OFF_TAX = 600

MULTIPLICITY = 50


def atm_machine(name: str):
    sum_ = START
    operation_count = 0

    while True:

        choice = int(input('Choose an action: '
                           '\n1 - Put money'
                           '\n2 - Take off money'
                           '\n3 - Exit\n'))
        match choice:

            case 1:
                if sum_ > WEALTH:
                    sum_ -= (sum_ - WEALTH) * WEALTH_TAX
                    msg = f'{name}, Since you have more than {WEALTH} on your account, we take off wealth tax {WEALTH_TAX}'
                    logger.info(msg)
                    print(msg)

                while True:
                    number = int(input('Enter sum you want to PUT: '))
                    if number % 50 == 0 and number > 0:
                        sum_ += number
                        msg = f'{name}, Operation completed successfully, you have {sum_} on your account'
                        logger.info(msg)
                        print(msg)
                        operation_count += 1
                        if operation_count % 3 == 0:
                            sum_ += number * EVERY_THIRD_OPERATION_TAX
                            msg = f'{name}, And since it was the third operation, we add you {EVERY_THIRD_OPERATION_TAX} and ' \
                                  f'now there is {sum_} on your account '
                            logger.info(msg)
                            print(msg)
                        break
                    else:
                        msg = f'{name}, Enter a summ multiples in {MULTIPLICITY} and not null'
                        logger.info(msg)
                        print(msg)

            case 2:
                if sum_ == 0:
                    msg = f'{name}, You have no money at all'
                    logger.info(msg)
                    print(msg)
                elif sum_ > 0:
                    if sum_ > WEALTH:
                        sum_ -= (sum_ - WEALTH) * WEALTH_TAX
                        msg = f'{name}, Since you have more than {WEALTH} on your account, we take off wealth tax {WEALTH_TAX}'
                        logger.info(msg)
                        print(msg)

                while True:
                    number = int(input('Enter sum you want to TAKE OFF: '))

                    if number <= 0 or number % MULTIPLICITY != 0:
                        msg = f'{name}, Enter a summ multiples in {MULTIPLICITY} and not null'
                        logger.info(msg)
                        print(msg)
                    else:
                        if number < MIN_TAKE_OFF_TAX / TAKE_OFF_TAX:
                            tax_sum = MIN_TAKE_OFF_TAX
                        elif number > MAX_TAKE_OFF_TAX / TAKE_OFF_TAX:
                            tax_sum = MAX_TAKE_OFF_TAX
                        else:
                            tax_sum = number * TAKE_OFF_TAX

                        if sum_ < number + tax_sum:
                            msg = f'{name}, You have not enough money on your account for this operation'
                            logger.info(msg)
                            print(msg)
                        else:
                            sum_ -= number + tax_sum
                            msg = f'{name}, Operation completed successfully. Summ on your account now is {sum_}'
                            logger.info(msg)
                            print(msg)
                            operation_count += 1
                            if operation_count % 3 == 0:
                                sum_ += number * EVERY_THIRD_OPERATION_TAX
                                msg = f'{name}, And since it was thethird operation, ' \
                                      f'we add you {EVERY_THIRD_OPERATION_TAX}' \
                                      f' and now there is {sum_} on your account'
                                logger.info(msg)
                                print(msg)
                            break

            case 3:
                break


def get_args():
    args = argparse.ArgumentParser(description='Получаем аргументы')
    args.add_argument('-n', '--name', default='Unknown')
    arg = args.parse_args()
    print(arg)
    return atm_machine(f'{arg.name}')


if __name__ == '__main__':
    # atm_machine('Айрат')
    get_args()
