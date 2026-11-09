"""Form for adding a cafe.

@file form.py
@brief The Flask-WTF form with its validators.
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.fields import SelectChoice
from wtforms.validators import URL, DataRequired

from coffee_and_wifi.constants import (
    COFFEE_CHOICES,
    MESSAGE_INVALID_URL,
    MESSAGE_REQUIRED,
    POWER_CHOICES,
    WIFI_CHOICES,
)
from coffee_and_wifi.domain.cafe import Cafe


def _required() -> DataRequired:
    return DataRequired(message=MESSAGE_REQUIRED)


def _choices(values: tuple[str, ...]) -> list[SelectChoice]:
    return [SelectChoice(value, value) for value in values]


class CafeForm(FlaskForm):  # type: ignore[misc]
    """Collects the data of a new cafe."""

    cafe = StringField("Cafe name", validators=[_required()])
    location = StringField(
        "Cafe Location on Google Maps (URL)",
        validators=[_required(), URL(message=MESSAGE_INVALID_URL)],
    )
    open_time = StringField("Opening Time e.g. 8AM", validators=[_required()])
    close_time = StringField("Closing Time e.g. 5:30PM", validators=[_required()])
    coffee_rating = SelectField(
        "Coffee Rating", choices=_choices(COFFEE_CHOICES), validators=[_required()]
    )
    wifi_rating = SelectField(
        "Wifi Strength Rating", choices=_choices(WIFI_CHOICES), validators=[_required()]
    )
    power_rating = SelectField(
        "Power Socket Availability",
        choices=_choices(POWER_CHOICES),
        validators=[_required()],
    )
    submit = SubmitField("Submit")

    def to_cafe(self) -> Cafe:
        """Return the submitted values as a cafe."""
        return Cafe(
            name=str(self.cafe.data),
            location=str(self.location.data),
            open_time=str(self.open_time.data),
            close_time=str(self.close_time.data),
            coffee=str(self.coffee_rating.data),
            wifi=str(self.wifi_rating.data),
            power=str(self.power_rating.data),
        )
