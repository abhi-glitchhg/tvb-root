from tvb.datasets import Record, Zenodo

#4263723


zenodo_client = Zenodo()


records = zenodo_client.get_record("4263723")

print(records)

records.download()


