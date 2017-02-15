import java.io.IOException;

public class CorpusGeneratorMain {
	
	private static InputFileReader reader;
	private static DataSearcher searcher;
	private static POST tagger;

	public static void main(String[] args) throws IOException,
			InterruptedException {
		reader = new InputFileReader(".htm");
		try {
			reader.loadFromFile();
		} catch (IOException e) {
			if (Configurations.showExceptions) {
				e.printStackTrace();
			}
		}

		searcher = new DataSearcher();
		tagger = new POST();
		
		CorpusGenerator generator = new CorpusGenerator();
		
		for (int i = 0; i < reader.anzahlDokumente(); i++) {
			System.out.println("_____________________Erfasse Dokument " + reader.dateiPfadAusgabe(i) + "..."); 
			searcher.setDocumentToReadFrom(reader.dokumentAusgabe(i),
					reader.dateiPfadAusgabe(i));
			searcher.extractData();
		
//			for (int y = 0; y < searcher.getNumberOfSongs(); y++) {
//				generator.createCorpusfileBody(searcher.getId(y), searcher.getTitle(y),
//						searcher.getText(y), searcher.getDate(y), searcher.getAlbum(y), searcher.getAuthor(y)); 
//			}
			//generator.generateCorpusFile("Corpus_Dylan" + searcher.getNumberOfSongs() ); 
			//sucher.schreibeDokument();
		//	searcher = new DataSearcher();
			//sucher.zeigeDokumentText();
		}
		for (int y = 0; y < searcher.getNumberOfSongs(); y++) {
		
			try {
				generator.createCorpusfileBody(searcher.getId(y), searcher.getTitle(y),
						tagger.analyzeSong(searcher.getText(y)), searcher.getDate(y), searcher.getAlbum(y), searcher.getAuthor(y), searcher.getFilePath(y));
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} 
		}
		
		generator.generateCorpusFile("Corpus_Dylan" + searcher.getNumberOfSongs() );
		
		System.out.println("VORGANG BEENDET. Das Programm kann nun geschlossen werden.---------------------------");

	}

}
