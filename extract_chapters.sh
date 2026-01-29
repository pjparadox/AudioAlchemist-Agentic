#!/bin/bash
DOC="input_quill/Freehaven Online - Ebook.doc"

strings "$DOC" | sed -n '2122,2289p' > input_quill/extracted/ch12.txt
strings "$DOC" | sed -n '2290,2388p' > input_quill/extracted/ch13.txt
strings "$DOC" | sed -n '2389,2773p' > input_quill/extracted/ch14.txt
strings "$DOC" | sed -n '2774,2870p' > input_quill/extracted/ch15.txt
strings "$DOC" | sed -n '2871,3268p' > input_quill/extracted/ch16.txt
strings "$DOC" | sed -n '3269,3332p' > input_quill/extracted/ch17.txt
strings "$DOC" | sed -n '3333,3438p' > input_quill/extracted/ch18.txt
strings "$DOC" | sed -n '3439,3786p' > input_quill/extracted/ch19.txt
strings "$DOC" | sed -n '3787,3936p' > input_quill/extracted/ch20.txt
strings "$DOC" | sed -n '3937,4037p' > input_quill/extracted/ch21.txt
strings "$DOC" | sed -n '4038,$p' > input_quill/extracted/epilogue.txt
