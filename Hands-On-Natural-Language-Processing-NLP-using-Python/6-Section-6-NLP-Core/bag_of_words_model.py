# Text representation models -Bag of Words Model
'''

Hello and welcome to this natural language processing tutorial and in this video we are finally going
to get started building our first text presentation model which is the bag of word's Model.
So say we have these three simple sentences right so

It is going to rain today.
Today I'm not going outside.
I'm going to watch the season premiere.


So these are the simple sentences.And now say you have to perform some kind of an NLP task using the sentences whether
the task is text classification or text summarize  or anything else.

So you know whatever you are going to do you are going to apply some kind of algorithm and that algorithm works mainly on numbers right.
It works on floating point or integer or whatever numbers and so on.

So that algorithm can actually directly work on the words or sentences that we have over here.So we can just fit in this
whole sentence and do some kind of analysis.So we need to convert all these different sentences into an intermediate
presentation or a model and then we can feed that model to some algorithm to do any kind of analysis right.
So let's find out how we can really use these three simple sentences to create the very simple bag of words model.

So the first thing that we're going to do is we will be pre processing  the sentences.Now if you look at the sentences
you can pretty much say that it's allready pre process right.
We have already removed the different punctuation marks and so on but you know we will do one more thing
which is we will convert all of these sentences into lowercase and after that we will you know pretty much have something like this.
All of these sentences are converted into lowercase.


And next what we going to do is we're going to tokenize each of the different sentences over here.
So after organizing we can have something like this you know. So we have this sentence one which is it is going to rain
today then sentence 2 and then sentence three.

And now we have to form and he still Rams out of all of these tokenize sentences so what is the histogram of them.
Well you have all these different words right.



So we are going to pick one word so we pick this word it right and then we are going to find out how
many times it appears in all of these sentences.Now as you can see it appears once and then it pretty much appears nowhere else right.
So it will have a value of 1 right.

Similarly we are going to look at is and then we are going to look at going and so on.
And we are pretty much going to be a dictionary where each of the different words will be keys and corresponding
to those keys we will have the values which will be the count of that particular word in the whole corpus of documents.
So this is how we are going to start building it.So initially we have the word it right.So it only appears once in all the different sentences.
So let's find out what is the next word or the next what is is.And you know we are pretty much doing all these iterations by sentence so we are getting all the words
from the first sentence first and then we will look into all the words in the second sentence and soon.

So is appears once going appears wants to appear as Von Sareen once to day ones and so on right.And now when you look at the second sentence.
So you have the first word which is today.Is today is all ready in our history.Right so we don't need to enter one more.Over here we can pretty much just increase the count of this existing today so we will have two day
of two.

And then we have another word which is I will write is not in the histogram so we would have to add it.So have I and the corresponding value is 1.
Similarly we have an over here which is also not in that dictionary.So we will have amond one and then we have a going well going is already in the history right.
So we are going to make this one as two and you know we we have not.Which does not appear over here so we will just add not as an other word and we will just add one over
here and so on then we have outside which is also not in the histogram and so on.

So this is how we are going to iterate through all the different sentences and we are going to create a histogram out of it.
So after we had pretty much done then we will have a whole histogram just like this.Right.So we have all the different words and up count of these words right.
The number of times this word appears in all the documents in the corpus.So now what we would have to do is we would have to sort this whole dictionary or histogram by the count.
So how can we do that.

Well as you can see that going has the highest count which is three.So when we start then going is going to appear at the top right.
So here we have going.Then we would have what is the maximum word.Well the next maximum word is two so we can have here two.Similarly after that we would have two day the night.
And then all the different words right over here right.


And you know when we are building this whole bag of cards model we really don't want to count all the
words you know we don't really want to consider all the different words that appear in the different documents.
We are going to consider some fixed number of words and you know when the reason is that say Here we have only say three sentences so the number of words that are what about 14.
What say you were analyzing about 50000 odd million sentences and so on.So there you will find words in the numbers of say seven K or 8 K and so on.
So you can really analyze on that huge amount of words right.So you need to reduce the amount of words and that is the reason why I'm showing you that how we can
really do that because you know you need to know when you are doing it on huge corpus of data.So you saw the whole list around you got this.
And now we have to filter it.So we have to filter it and we are here considering then most frequent words.
So you know these are the most frequent words.So we are not going to consider any of these four words.

So after we filter it we will have something that pretty much looks like this.And now it's using this whole dictionary.
We are going to create a matrix on the back of this model.Right.And this is how this matrix is going to look like.
So here as you can see we have all the frequent words as the columns of the matrix right.So we have go to today.I am.It is raining outside and so on.

- Histogram of words with count
- Make matrix of most frequency words - words - column and Row Words/Documents (doc 1,doc 2,doc 3 etc)


And then in the rows we have the Diffrent documents so we have three documents.

So here this is document 1.

This is document 2 and this is documentary.

So now let's find out how are we going to fill out this whole matrix so you know this is the first sentence

right.

It is going to rain today.

And now we're going to go through the sentence word by word rate so we will first see this word it then

Lucy the word is then the word going then the word to and so on and we will just figure out whether

you know this word appears over here in the matrix or not.

And if this word appears then we are going to put a one over here.

So you know let's just find out how we are really going to do that.

So first we have the word going right.

Now this word going doesn't appear in the first sentence.

Well it does appear so we can just put a one.

Next we have the word do.

Does the word appear in the first sentence.

Well it does.

So you can again put here another one.

Then we have the word today.

Does it appear in the first sentence.

Well it does.

So we will put here another one and then we have the word I.

Well I does not appear in the sentence so we can put here 0 0 if the word appears.

It's a 1.

If the word does not appear then it's zero.

Similarly and does not appear superhero 0 it appears.

So you'll have a 1.

Is appears to have another one.

Green appears to have another one not does not appear so we'll get a zero.

And outside also does not appear so we'll get another zero.

Similarly we can fill this for the second sentence as well.

You know just like this.

So we'll have ones when the word appears we'll have zeros when the word does not appear.

And similarly we will have this whole matrix right.

And this is our verifiers more right.

So in the columns you have all the frequent words and in the rows you have all the different documents

and you have ones and zeros corresponding to whether the word appears in the document or the word does

not appear in the document.

So initially we had this right.

This matix is called bag of words model.
We have these three sentences and we converted it into this bag of words model and you can now feed
you know feed this model to any kind of machine learning algorithms are in algorithms and analyze the
sentences.

So you know when we are really working with huge corpus of data so when we are doing the classification
thing then you will find out that we will be looking into a huge corpus of data with about 50000 or40000 different rows of text there.
We won't really have infrequent words rather we would have about 2000 or 3000 frequent words right will
have a matrix of say 40000 rows and 3000 columns and we would be doing analyses on those matrices. So this is pretty much it.

This is how you build the Bag of  model and starting the next video we will find out how we can

really build our own bag of words  model in Python directly from scratch without using any kind of libraries.

So that's it.

And I will see you in the next one.

'''