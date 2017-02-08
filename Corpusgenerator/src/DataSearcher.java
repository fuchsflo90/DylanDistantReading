import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.safety.Whitelist;

public class DataSearcher {

		// Dokument roh
		private String docText;
		private Document doc;
		private Element songText;

		// Extraktion Metadaten
		private String filePath;
		
		Songs corpus;

		public DataSearcher() {
			corpus = new Songs();
		}

		public void setDocumentToReadFrom(Document doc, String filePath) {
			this.doc = doc;
			this.filePath = filePath;
	//		if (Configurations.debugHTMLdocDOM) {
	//		
	//			for( Element element : doc.getElementsByAttributeValue("style", "display:none") )
	//			{
	//			    element.remove();
	//			}
				
				
//				//http://stackoverflow.com/questions/5640334/how-do-i-preserve-line-breaks-when-using-jsoup-to-convert-html-to-plain-text
//				docText = Jsoup.clean(doc.html(), "", Whitelist.none(), new Document.OutputSettings().prettyPrint(false))
//						.replaceAll("&nbsp;", " ")
//						.replaceAll("\\"+Character.toString('\u00AD'), "")
//						.replaceAll("([N,n]ationalrat,.X.*)(\\s*.*\\s*)(.*[S,s]eite.\\d*)", "")
//						.replaceAll("(<|>)", "")
//						.replaceAll("\\*", "");
//						//.replaceAll("(\\s{2,})"," ") + " ";
//				//System.out.println(dokText);
	//		}
		}

		public void extractData() {
			//doc.normalise();
			//dokText = doc.html();
			// sucheSitzungsStart();
			generateSongList(doc);

		}
		
		private String extractDate(String input){
			String output = "";
			Matcher match = findeTextausschnitte("\\((.*)\\)", input);
			if (match.find()){
				//output = input.substring(match.end(), input.length()-1);
				output = match.group(1);
				output = output.substring(0, 4);
				//System.out.println(dokText);
			}
			
			return output;
		}
		
		private String cleanAlbum(String input){
			String output = "";
			output = input.replaceAll("\\((.*)\\)", "");
			output = output.substring(0, output.length()-1);
			
			return output;
		}
		
		// Findet alle Redner, deren Reden von einem Ereignis unterbrochen werden
		private void generateSongList(Document doc) {
			
			String title = "title";
			String text = "text";
			String date = "date";
			String album = "album";
			String author = "author"; 
			
			title = cleanText(doc.getElementsByAttributeValue("id", "song-header-title").toString());
			text = cleanText(doc.getElementsByAttributeValue("class", "lyricbox").toString());
			date = extractDate(cleanText(doc.getElementsByAttributeValue("id", "song-header-container").toString()));
			try{
				album = cleanAlbum(cleanText(doc.getElementsByAttributeValue("id", "song-header-container").get(0).getElementsByTag("i").toString()));
			}catch(IndexOutOfBoundsException e){
				System.out.println(e.toString());
				album = "unknown";
			}
				// some files don't credit an author, thats why a try/catch block is needed
			try{	
				author = cleanText(doc.getElementsByAttributeValue("class", "song-credit-box").get(0).child(0).child(0).child(1).toString());
			}catch(IndexOutOfBoundsException e){
				System.out.println(e.toString());
				author = "unknown";
			}
			// System.out.println("Der Author: " + author );
			
			corpus.newSong(title, text, date, album, author, filePath);
		}
		
		//TODO
		public String cleanText(String uncleanText){
			String cleanText = "";
			
			cleanText = Jsoup.clean(uncleanText, "", Whitelist.none(), new Document.OutputSettings().prettyPrint(false))
					.replaceAll("&lt;br&gt;", "")
					.replaceAll("\\"+Character.toString('\u00AD'), "")
					.replaceAll("(<|>)", "")
					.replaceAll("\\*", "")
					.replaceAll("&amp;amp;", "");

			return cleanText;
		}

		
		public int getNumberOfSongs(){
			return corpus.getNumberOfSongs();
		}

		public String gebeProtokolldatum() {
			return corpus.gebeZeitraum();
		}

		public String gebeSitzungsnummer() {
			return corpus.gebeSitzungsnummer();
		}

		public String gebePeriode() {
			return corpus.gebeRegierungsperiode();
		}
		
		public int getId(int index) {
			try {
				return corpus.getId(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return 0;
			}
		}

		public String getTitle(int index) {
			try {
				return corpus.getTitle(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		
		public String getText(int index) {
			try {
				return corpus.getText(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		
		public String getDate(int index) {
			try {
				return corpus.getDate(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		public String getAlbum(int index) {
			try {
				return corpus.getAlbum(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		public String getAuthor(int index) {
			try {
				return corpus.getAuthor(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		
		public String getFilePath(int index){
			return corpus.getFilePath(index);
		}

		private Matcher findeTextausschnitte(String regex, String textdatenRoh) {
			Pattern pattern = Pattern.compile(regex);
			Matcher matcher = pattern.matcher(textdatenRoh);
			return matcher;
		}
		
		public void schreibeDokument() throws IOException{
			 File newDoc = new File("./outDoc/" + corpus.gebeRegierungsperiode() + "_" + corpus.gebeSitzungsnummer()
			 + "_" + corpus.gebeZeitraum() + ".html");
			 OutputStreamWriter out = new OutputStreamWriter(new FileOutputStream(newDoc), "utf-8");
			 out.write(doc.html());
			 out.close();
		}
}
