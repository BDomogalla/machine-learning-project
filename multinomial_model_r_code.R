install.packages("nnet")
library("nnet")

data = read.csv("Data/personality_traits.csv", header = TRUE)
View(data)

model_fit <- multinom(Education ~ Daily_events + Prioritising_workload + Writing_notes + Workaholism +
                        Thinking_ahead + Final_judgement + Reliability + Keeping_promises + Loss_of_interest + 
                        Friends_versus_money + Funniness + Fake + Criminal_damage + Decision_making + 
                        Elections + Self_criticism + Judgment_calls + Hypochondria + Empathy + Eating_to_survive + 
                        Giving + Compassion_to_animals + Borrowed_stuff + Loneliness + Cheating_in_school + 
                        Health + Changing_the_past + God + Dreams	+ Charity + Number_of_friends + Waiting +
                        New_environment + Mood_swings + Appearence_and_gestures + Socializing + Achievements + 
                        Responding_to_a_serious_letter + Children + Assertiveness + Getting_angry + 
                        Knowing_the_right_people + Public_speaking + Unpopularity + Life_struggles + Happiness_in_life +
                        Energy_levels + Small_big_dogs + Personality + Finding_lost_valuables + Getting_up + Interests_or_hobbies +
                        Parents_advice + Questionnaires_or_polls, data = data)

summary_table <- summary(model_fit)
coef <- coef(summary(model_fit))

z <- summary(model_fit)$coefficients/summary(model_fit)$standard.errors

p <- (1 - pnorm(abs(z), 0, 1))*2
p

write.csv(p,"multinom_p_values_education_MOSHER.csv", row.names = TRUE)

write.csv(coef,"multinom_coef_values_education_MOSHER.csv", row.names = TRUE)



