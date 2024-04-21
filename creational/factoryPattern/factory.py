from creational.factoryPattern import JsonSerializer, XmlSerializer
from creational.factoryPattern import Song


class SerializerFactory:
    @staticmethod
    def get_serializer(format: str):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            raise ValueError(format)


factory = SerializerFactory()


class ObjectSerializer:
    def serialize(self, serializable, format: str):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


def main():
    song = Song(song_id='1', title='C4', artist="ATL")
    serializer = ObjectSerializer()
    songJson = serializer.serialize(song, 'JSON')
    songXml = serializer.serialize(song, 'XML')
    print(f"songJson: {songJson}\nsongXml: {songXml}")


if __name__ == "__main__":
    main()