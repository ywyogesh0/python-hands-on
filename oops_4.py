from abc import ABC, abstractmethod


class Source(ABC):

    def __init__(self, source_id):
        self.source_id = source_id

    @abstractmethod
    def ingest(self):
        pass

class KafkaSource(Source):

    def ingest(self):
        pass


class FileSource(Source):

    def ingest(self):
        pass


class Transformer(ABC):

    def __init__(self, transform_id,):
        self.transform_id = transform_id

    @abstractmethod
    def transform(self, data):
        pass


class PaymentTransformer(Transformer):

    def transform(self, data):
        pass


class Sink(ABC):

    def __init__(self, sink_id):
        self.sink_id = sink_id

    @abstractmethod
    def sink(self, transformed_data):
        pass

class BigQuerySink(Sink):

    def sink(self, transformed_data):
        pass


class FileSink(Sink):

    def sink(self, transformed_data):
        pass


class Pipeline:

    def __init__(self, source, transformer, sink):
        self.source = source
        self.transformer = transformer
        self.sink = sink

    def run(self):
        data = self.source.ingest()
        transformed_data = self.transformer.transform(data)
        self.sink.sink(transformed_data)

if __name__ == "__main__":
    p = Pipeline(
        source=FileSource(source_id="source_id"),
        transformer=PaymentTransformer(transform_id="transform_id"),
        sink=BigQuerySink(sink_id="sink_id")
    )

    p.run()