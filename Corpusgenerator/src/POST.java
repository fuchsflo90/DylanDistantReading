/*package stanfordtagger;
*/

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.List;

import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.ling.TaggedWord;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.io.ReaderInputStream;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.process.CoreLabelTokenFactory;
import edu.stanford.nlp.process.DocumentPreprocessor;
import edu.stanford.nlp.process.PTBTokenizer;
import edu.stanford.nlp.process.TokenizerFactory;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;

public class POST {

	private String taggerModel = "./models/english-bidirectional-distsim.tagger";
	private MaxentTagger tagger = new MaxentTagger(taggerModel);
	
  public String analyzeSong(String song) throws Exception {
	String output = "";
	    TokenizerFactory<CoreLabel> ptbTokenizerFactory = PTBTokenizer.factory(new CoreLabelTokenFactory(),
										   "untokenizable=noneKeep");
	    
	    InputStream stream = new BufferedInputStream( new ReaderInputStream( new StringReader(song)));
	    BufferedReader r = new BufferedReader(new InputStreamReader(stream, "utf-8"));
	    
	    DocumentPreprocessor documentPreprocessor = new DocumentPreprocessor(r);
	    documentPreprocessor.setTokenizerFactory(ptbTokenizerFactory);
	     
	    for (List<HasWord> sentence : documentPreprocessor) {
	    	//String sentenceString = Sentence.listToString(sentence); 	
	    	//System.out.println(sentenceString);
	    	List<TaggedWord> tSentence = tagger.tagSentence(sentence);
	    	//out_POS.write(Sentence.listToString(tSentence, false) + "\n");
	    	output = output + Sentence.listToString(tSentence, false) + "\n";
	    	//System.out.println(Sentence.listToString(tSentence, false));
	    }
	    return output;
 }
}
 