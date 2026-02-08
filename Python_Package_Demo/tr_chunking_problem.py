from dataclasses import dataclass
from typing import Optional

@dataclass
class Chunk():
    body: str
    h1: str
    h2: Optional[str]
    h3: Optional[str]


def retrieve_chunks(keyword: str, document_str: str) -> list[Chunk]:
    lines = document_str.split("\n")

    chunks = []
    current_h1 = None
    current_h2 = None
    current_h3 = None

    for line in lines:
        print("Line:", line)
        if line.strip().startswith("# "):
            current_h1 = line.strip()[2:]
            current_h2 = None
            current_h3 = None
        elif line.strip().startswith("## "):
            current_h2 = line.strip()[3:]
            current_h3 = None
        elif line.strip().startswith("### "):
            current_h3 = line.strip()[4:]
        else:
            if line.strip() == "":
                continue
            # if keyword.lower() in line.lower():
            chunks.append(Chunk(
                body=line.strip(),
                h1=current_h1,
                h2=current_h2,
                h3=current_h3
            ))
        print("Current H1:", current_h1)
        print("Current H2:", current_h2)
        print("Current H3:", current_h3)
        print("chunks so far:", chunks)
        

    return chunks


if __name__ == "__main__":
    doc_str = """
        # Introduction

        This document explains transformers.

        ## Attention
        
        Attention is the core idea.

        ### Self Attention
        
        Self attention allows tokens to attend to each other.

        ## Training
        
        Training requires large datasets.
        """
    
    keyword = "attention"

    chunks = retrieve_chunks(keyword, doc_str)
    print("Keyword:", keyword)
    for chunk in chunks:
        print("H1:", chunk.h1)
        print("H2:", chunk.h2)
        print("H3:", chunk.h3)
        print("Body:", chunk.body)
        print("---")