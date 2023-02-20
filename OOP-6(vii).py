class Lesson:
    # PRIVATE LessonType, Instructor : STRING

    def __init__(self, LessonType_D, Instructor_D):

        self.LessonType = LessonType_D
        self.Instructor = Instructor_D

    def GetLessonType(self):
        return self.LessonType

    def GetInstructor(self):
        return self.Instructor

    def SetLessonType(self, NewLesson):
        self.LessonType = NewLesson

    def SetInstructor(self, NewInstructor):
        self.Instructor = NewInstructor

    def GetFee(self, SkillLevel):

        if SkillLevel == "B":
            return 45
        elif SkillLevel == "I":
            return 50
        elif SkillLevel == "A":
            return 55
        else:
            return -1

# DECLARE LessonArray[1,9] : Array

