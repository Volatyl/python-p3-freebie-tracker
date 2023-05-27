from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

company_dev = Table(
    'company_dev', Base.metadata,
    Column('company_id', ForeignKey('companies.id')),
    Column('dev_id', ForeignKey('devs.id'))
)


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    devs = relationship('Dev', secondary='company_dev',
                        back_populates='companies')
    freebies = relationship('Freebie', back_populates='company')

    def __repr__(self):
        return self.name

    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(item_name=item_name, value=value)

        self.freebies.append(freebie)
        dev.freebies.append(freebie)

        session.add(freebie)
        session.commit()

    @classmethod
    def oldest_company(cls):
        return session.query(Company).order_by(Company.founding_year).first()


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    companies = relationship(
        'Company', secondary='company_dev', back_populates='devs')
    freebies = relationship('Freebie', back_populates='dev')

    def __repr__(self):
        return f'<Dev: {self.name}>'

    def received_one(self, item_name):
        for freebie in self.freebies:
            if item_name == freebie.item_name:
                return True
        return False

    def give_away(self, dev, freebie):
        if self.name == freebie.dev.name:
            freebie.dev = dev
            session.commit()
            return 'Done'
        return False


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')

    def __repr__(self):
        return self.item_name

    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'


Sam = session.query(Dev).filter_by(name='Sam').first()
Ken = session.query(Dev).filter_by(name='Ken').first()
folio = session.query(Freebie).filter_by(item_name='folio').first()
Tv = session.query(Freebie).filter_by(item_name='Tv').first()

print(Ken.give_away(Sam, folio))


# Tesla = session.query(Company).filter_by(name='Tesla').first()

# truck = Tesla.give_freebie(Sam, 'Truck', 6345)
