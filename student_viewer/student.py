from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    last_name: str
    level: str
    age: int
    units: int
    grade_points: int

    def get_grade_point_average(self) -> float:
        weighted_gpa = self.grade_points / self.units
        if weighted_gpa > 4.00:
            return 4.00
        else:
            return weighted_gpa
