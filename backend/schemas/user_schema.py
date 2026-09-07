from marshmallow import Schema, fields, validate

class RegisterSchema(Schema):
    name = fields.String(
        required=True,
        validate=validate.Length(min=2, error="El nombre debe tener al menos 2 caracteres.")
    )
    email = fields.Email(
        required=True,
        error_messages={"required": "El email es obligatorio.", "invalid": "Formato de email inválido."}
    )
    password = fields.String(
        required=True,
        validate=[
            validate.Length(min=8, error="La contraseña debe tener al menos 8 caracteres."),
            validate.Regexp(
                r'^(?=.*[A-Za-z])(?=.*\d).+$',
                error="La contraseña debe contener al menos una letra y un número."
            )
        ]
    )
