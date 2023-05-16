import datetime
from typing import Optional, Iterable, Union, Counter
import collections 
import math


class Sample:
    """Abstract superclass for all sample classes"""
    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        species: Optional[str] = None
    ) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification: Optional[str] = None

    def __repr__(self) -> str:
       
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}"
            
            f")"
        )
    
    def classify(self, classification: str) -> None:
        self.classification = classification
    
    def matches(self) -> bool:
        return self.species == self.classification

class TrainingknownSample:
    pass

class KnownSample(Sample):
    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        species: str,
    ) -> None:
         super().__init__(
             sepal_length=sepal_length,
             sepal_width=sepal_width,
             petal_length=petal_length,
             petal_width=petal_width
         )
         self.species = species

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}"
      
            f")"
        )

class UnknownSample(Sample):
    """Sample provided by an user, not yet classified"""
    pass

class ClassifiedSample(Sample):
    def __init__(self, classification, sample: UnknownSample) ->None:
        super().__init__(
            self.sepal_length = sample.sepal_length
            self.sepal_width = sample.sepal_width
            self.petal_length = sample.petal_length
            self.petal_width = sample.petal_width
        )
        self.classification = classification

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}"
            f"classification={self.classification!r}"
        )

class TestKnownSample(KnownSample):
    def __init__( self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        classification: Optional[str] = None
    ) -> None

    super().__init__(self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    )
    self.classification= classification
    pass

    def __init__(self) -> str:
        pass

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}"
            f"classification={self.classification!r}"
        )
    def matches(self) ->bool:
        return self.species == self.classification


class Distance:
    def distance(self, s1:Sample,s2: Sample) -> float:
        pass

class ED(Distance):
    def distance(self, s1:Sample,s2: Sample) -> float:
        return math.hypot(
            s1.sepal_length - s2.sepal_length,
            s1.sepal_width - s2.sepal_width,
            s1.petal_length - s2.petal_length,
            s1.petal_width - s2.petal_width
        )
    pass


class MD(Distance):
    def distance(self, s1:Sample,s2: Sample) -> float:
        return sum([
            abs(s1.sepal_length - s2.sepal_length),
            abs(s1.sepal_width - s2.sepal_width),
            abs(s1.petal_length - s2.petal_length),
            abs(s1.petal_width - s2.petal_width)
        ])
    pass

class CD:
    pass
class SD:
    pass

class Hyperparameter:
    def __init__(self, k: int,algorithm: Distance, training: "TrainingData") -> None:
        self.k = k
        self.algorithm = algorithm
        self.data: TrainingData = training
        self.quality: float

    def classify(self, sample: Union[UnknownSample, TestingKnownSample]): -> str:
        training_data = self,data
        if not training_data:
            raise RuntimeError("No Training object")
        distances: list[tuple[float, TrainingKnownSample]] = \
            sorted(
                    (self,algorithm.distance(sample, known),known) for known in training_data.training 
            )
        """TODO: k-NN 알고리즘"""
        k_nearest: tuple[str] = (known.species for _, known in distances[:self.k])
        frequency: Counter[str] = collections.Counter(k_nearest)
        best_fit, *others = frequency.most_common()
        species, votes = best_fit
        return species
    def test(self) -> None:
        training_data: Optional["TrainingData"] = self.data
        if not training_data:
            raise RuntimeError("")
        pass_count, fail_count = 0, 0
        for sample in self.data.testing_data.testing:
            sample.classification = self.classify(sample)
            if sample.matches():
                pass_count += 1
            else:
                fail_count += 1
        self.quality = pass_count / (pass_count + fail_count)


class TrainingData:
    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded: datetime.datetime
        self.tested: datetime.datetime
        self.training: list[Sample] = []
        self.testing: list[Sample] = []
        self.tuning: list[Hyperparameter] = []

    def load(self, raw_data_source: Iterable[dict[str, str]]) -> None:
        for n, row in enumerate(raw_data_source):
            if n%5 ==0:
                test +TestingKnownSample()
                species = row["species"]
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"]),
                species=row["species"]
            )
            
                self.testing.append(test)
            else:
                test  (species = row["species"]
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"]),
                
                )
                self.training.append(test)
        self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)

    def test(self, parameter: Hyperparameter) -> None:
        parameter.test()
        self.tuning.append(parameter)
        self.tested = datetime.datetime.now(tz=datetime.timezone.utc)

    def classify(self, parameter: Hyperparameter, sample: Sample) -> Sample:
        classification = parameter.classify(sample)
        sample.classify(classification)
        return sample




test_sample = """
>>> x = Sample(1.0, 2.0, 3.0, 4.0)
>>> x
UnknownSample(sepal_length=1.0, sepal_width=2.0, petal_length=3.0, petal_width=4.0, species=None)
"""

__test__ = {
    name: case for name, case in globals().items() if name.startswith("test_")
}

# if __name__ == "__main__":
#     sample = Sample(2.0, 2.0, 20.2, 30.1, "Virginica")
#     print(sample.classify("Sentosa"))
#     print(sample.matches())
