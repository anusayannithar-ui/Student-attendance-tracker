CREATE DATABASE IF NOT EXISTS vidyananda_student_attendance_tracker;
USE vidyananda_student_attendance_tracker;

CREATE TABLE IF NOT EXISTS students (
    student_id_hashed_qr_code INT,
    student_id INT ,
    student_name VARCHAR(100) ,
    class VARCHAR(5),
    phone_no_of_guardian VARCHAR(20),

    PRIMARY KEY(student_id_hashed_qr_code,student_id)
);
CREATE TABLE  IF NOT EXISTS attendance (
     student_id INT,
     date_of TIMESTAMP,
     arrival TIMESTAMP ,
     departure TEXT DEFAULT 'STILL IN SCHOOL',
     FOREIGN KEY (student_id) REFERENCES students(student_id)
);




