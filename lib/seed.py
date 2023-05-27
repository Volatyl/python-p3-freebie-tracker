#!/usr/bin/env python3


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Dev, Company, Freebie, company_dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(Dev).delete()
    # session.query(Company).delete()
    # session.query(Freebie).delete()

    # HP = Company(name='HP', founding_year=1996)
    # Samsung = Company(name='Samsung', founding_year=1998)
    # Tesla = Company(name='Tesla', founding_year=2001)

    # Ken = Dev(name='Ken')
    # Sam = Dev(name='Sam')

    # session.add_all([HP, Samsung, Tesla, Ken, Sam])
    # session.commit()

    # mouse = Freebie(item_name="mouse", value=40, dev=Ken, company=HP)
    # car = Freebie(item_name="car", value=23000, dev=Ken, company=Tesla)
    # galaxy10 = Freebie(item_name="galaxy10", value=40,
    #                    dev=Sam, company=Samsung)
    # folio = Freebie(item_name="folio", value=340, dev=Sam, company=HP)

    # session.add_all([mouse, car, galaxy10, folio])
    # session.commit()

    # HP.devs.append(Ken)
    # HP.devs.append(Sam)
    # Samsung.devs.append(Sam)
    # Tesla.devs.append(Ken)

    # session.commit()

    # x = session.query(Freebie).filter_by(item_name='mouse').first()

    # print(x.print_details())

    
