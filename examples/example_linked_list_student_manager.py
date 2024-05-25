import context

from adt_applications.linked_list_student_manager import LinkedListStudentManager
from adt_applications.linked_list_student_manager import Student


def sampling():
    llsm = LinkedListStudentManager()
    s_01 = Student("SE196855", "Hoang Dinh Duy Anh")
    s_02 = Student("SE196866", "Someone Else Not Me")
    llsm.insert_first(s_01)
    llsm.insert_first(s_02)
    llsm.update_student_by_id("SE196855", "Hoang Dinh Duy Anh", 10.0)
    llsm.display_students()
    search_result = llsm.search_student_by_id('SE196855')
    print(search_result.data)


if __name__=='__main__':
	sampling()
