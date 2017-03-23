#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, random

def getRandomFortune():
    fortunes = [
        "You will be hungry again in an hour.",
        "About time I got out of that cookie.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "Fortune not found: Abort, retry ignore?",
        "Everyone has a photographic memory. Some just don't have film.",
        "You will read this and say 'Geez, I could come up with better fortunes than that!'",
        "The fortune you seek is in another cookie.",
        "Ignore the previous cookie.",
        "You are about to become $8.95 poorer. ($10.95 if you had the buffet)",
        "You have rice in your teeth.",
        "You laugh now, wait until you get home.",
        "I cannot help you, for I am just a cookie.",
        "Next time, order the shrimp."
    ]

    fortune = fortunes[random.randrange(0,len(fortunes))]
    return fortune

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortuneSentence = "Your fortune: " + fortune
        fortuneParagraph = "<p>" + fortuneSentence + "</p>"

        luckyNumber = "<strong>" + str(random.randrange(1,101)) + "</strong>"
        numberSentence = 'Your lucky number: ' + luckyNumber
        numberParagraph = "<p>" + numberSentence + "</p>"

        newCookie = "<a href='.'><button>Another cookie, please!</button></a>"

        content = header + fortuneParagraph + numberParagraph + newCookie

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
