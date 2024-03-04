import csv
import WebScraping
import time


def main():

    sc = WebScraping.Scraper()
    pageNum = 48

    data = []

    with open('fianl_car_data.csv', 'w', encoding = 'utf-8-sig') as f:

        thewriter = csv.writer(f)

        thewriter.writerow(sc.columns)
        print(sc.columns)

        for i in range(1, pageNum):
            if i <= 10:
                sc.set_url(sc.get_url()[:len(sc.get_url()) - 1] + str(i))
            else:
                sc.set_url(sc.get_url()[:len(sc.get_url()) - 2] + str(i))

            sc.load_url()
            sc.read_data()

            for h in sc.get_hrefs():

                data.append(sc.get_info("http://www.emlakjet.com/" + h))
                print(sc.get_info("http://www.emlakjet.com/" + h))

            sc.dump_hrefs()
            print(str(i) + "INFORMATION RECEIVED FROM THE PAGE ---------------------------")

        # write the data
        thewriter.writerows(data)


if __name__ == '__main__':
    main()